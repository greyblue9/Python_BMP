notice = """
  Mirror the top-left part of a BMP
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
        loadBMP,
        mirrortopleft,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/assets/tanuki.bmp')
        mirrortopleft(bmp)
        file = 'HelloMirrorTopLeft.bmp' # file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()


