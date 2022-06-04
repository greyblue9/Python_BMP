notice = """
 Hello World Dot Rainbow Sideways Font
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
        plotstringsidewayasdots,
        getcolorname2RGBdict,
        font8x8,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 70, 840 # bitmap size
        bmp = newBMP(mx, my, 24) # RGB bitmap
        c = getcolorname2RGBdict()
        colors = (c['brightred'],
                  c['brightorange'],
                  c['brightyellow'],
                  c['brightgreen'],
                  c['cyan'],
                  c['brightblue'],
                  c['brightmagenta'])
        plotstringsidewayasdots(bmp,
                10, 770, # position the text
                'Hello World!!', # random text
                7, # uint font size multiplier
                1, # uint space between pixels
                0, # uint default space between char
                colors,
                font8x8)
        file = 'HelloWorldDotsrainbowsideways.bmp' #file name
        saveBMP(file,bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()