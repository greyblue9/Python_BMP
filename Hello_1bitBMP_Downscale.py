notice = """
  Downsample an image to 1 bit Demo
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
        reduce24bitimagebits as f,
        getfuncmetastr as meta
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        file = f'{rootdir}/assets/somebody.bmp'
        newfile = '1bitBMP.bmp'
        bits= 1 # valid values are 8,4,1
        threshold = 8 # in computing new palette how far apart should colors be
        usemono = False # can apply a mono filter
        f(file, newfile, bits, threshold, usemono) # magic takes time
        print(f'All done close {imgedt} to finish')
        ret = proc.call([imgedt, newfile])

if __name__=="__main__":
        main()