notice = """
          Hello Globe Demo
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
        thickroundline,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 200 # bitmap size
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        p1 = (12,12) # 1st point as (x,y)
        p2 = (mx -12, my-12) # 2nd point as (x,y)
        penradius = 10
        color = 13
        thickroundline(bmp, p1, p2, penradius, color) # all unsigned
        #Python_BMP.BITMAPlib.thickroundline(bmp bytearray,p1 xy-tuple,p2 xy-tuple,penradius int,color int)
        file = 'HelloThickroundLine.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()


