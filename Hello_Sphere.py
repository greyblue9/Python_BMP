#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of running script
        mx=200 # bitmap size x
        my=mx # bitmap size y = x square bitmap
        bmp=b.newBMP(mx,my,24) # 24 bit BMP
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r=x-12 # radius = x - 12 
        rgbfactors=(.4,1,.7) # unsigned floats 0 to 1 -> (r,g,b)
        b.sphere(bmp,x,y,r,rgbfactors) # bmp is unsigned byte array
        file='HelloSphere.bmp' # file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


