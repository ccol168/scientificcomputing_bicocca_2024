from setuptools import setup, find_packages

setup(name='GameOfLifeBicocca',
      description='A tool to output Game of Life animations',
      url='https://github.com/ccol168',
      author='Claudio Coletta',
      author_email='colettaclaudio11@gmail.com',
      license='MIT',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])
