notice = """
Hello Earth with upsidedown text Demo
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
        plotstring,
        plotstringupsidedown,
        font8x14,
        font8x8,
        getcolorname2RGBdict,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        fontsize = 4 # font size
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 0 # space bitmap font characters (0 = default)
        plotstring(bmp, 5, 25,
                'Hello', fontsize, pixspace, charspace,
                c['brightred'], font8x14)
        plotstringupsidedown(bmp, 5, 85,
                'World', fontsize, pixspace, charspace,
                c['brightyellow'], font8x8)
        file = 'HelloEarthDownUpsidedowntext.bmp' #file name
        saveBMP(file,bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()



