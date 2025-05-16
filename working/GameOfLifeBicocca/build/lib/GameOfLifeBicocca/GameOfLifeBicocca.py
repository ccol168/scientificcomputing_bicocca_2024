import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class GameOfLife :

    def __init__(self,n) :
        self.fTable = np.zeros((n,n),dtype=int)
        self.fSize = n

    def Print(self) :
        print(self.fTable,"\n")

    def Initialize(self,listin) :
        NRow, NCol = zip(*listin)
        self.fTable[NRow,NCol] = 1 

    def InitializeRandom(self,NPoints) :
        listin = np.random.randint(0,self.fSize,size=(NPoints,2))
        self.Initialize(listin)

    def Update(self) : 
        kernel = np.array([ #kernel to multiply to the whole table 
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ])
        padded_Table = np.pad(self.fTable, pad_width=1, mode='constant', constant_values=0) #padded the starting state matrix
        sliding_windows = np.lib.stride_tricks.sliding_window_view(padded_Table, (3, 3)) #passes a sliding window of 3x3 matrix through the whole table 
        sums = (np.sum(sliding_windows*kernel,axis=(2,3))) #gives back a table containing the sums of kernel*window (basically tells how many points are adjacent to the given position)
        conditions = [
            (self.fTable == 1) & ((sums < 2) | (sums > 3)) ,
            (self.fTable == 1) & ((sums == 2) | (sums == 3) ) ,
            (self.fTable == 0) & (sums == 3) ,
            (self.fTable == 0) & (sums != 3)
        ]
        results = [0,1,1,0]

        self.fTable = np.select(conditions,results)

    def GetTable (self) :
        return self.fTable
        

    def PlaySteps(self,outfile,NSteps,imgsize=(5,5),timeInterval = 500) : #plays the game and gives back the animation of the game
        
        fig, ax = plt.subplots(figsize=imgsize)
        cax = ax.imshow(self.GetTable(), cmap='Greys')
        
        def init() :
            cax.set_data(self.GetTable())
            return [cax]
        
        def update(frames):
            if frames == 0: #avoid updating the first time
                return [cax]
            
            self.Update()
            cax.set_data(self.GetTable())
            if frames == NSteps - 1 : #necessary to avoid a weird behavior of FuncAnimation that does not stop after NSteps 
                plt.close(fig)
            #print(Tables[frames])
            return [cax]
              
        ani = FuncAnimation(fig, update, init_func=init, frames=NSteps, interval=timeInterval, blit=True)
        
        if (outfile == None ) :
            plt.show()
        else :
            ani.save(outfile)

        return ani
    


if __name__ == "__main__" :
    Game = GameOfLife(20)
    Game.Initialize([(0,0),(2,0),(1,1),(1,2),(2,1)])
    Game.PlaySteps("Test.mp4",50,timeInterval=200)


