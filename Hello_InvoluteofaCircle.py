notice = """
   Hello Involute of a Circle Demo
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""

from Python_BMP.BITMAPlib import(
        newBMP,
        pi,
        centercoord,
        plotlines,
        circleinvolutevert as f,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500 # bitmap size
        bmp = newBMP(mx, my, 4) # 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{fname}.bmp' # file name
        d = 1/120 # angle increment
        lim = pi * 20 + d # angle limit
        color = 10
        plotlines(bmp,
                f(x, y, # position the circle involute
                 3, # control size of step
                 d , lim), # angle step and limit
                color) # connect the dots with lines
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()