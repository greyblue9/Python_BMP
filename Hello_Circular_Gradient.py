#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx=512 #bitmap size
        my=mx
        bmp=b.newBMP(mx,my,24)
        mx,my=mx-1,my-1 #max-1 for screen
        cx,cy=mx>>1,my>>1 #div by 2
        r=cx
        b.gradcircle(bmp,cx,cy,r,[255,0],[1,.25,.5])
        file='HelloCircularGradient.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


