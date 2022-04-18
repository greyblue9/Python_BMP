#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        mx=my=250 # x=y square bmp
        file='HelloOctahedra.bmp' # some random file name as string
        bmp=b.newBMP(mx,my,4) # RGB bmp
        cenpt=b.centercoord(bmp) # helper method to get center of a bitmap
        cf=b.getRGBfactors() # color info with presets
        d,translationvector=400,[0,0,200] # be careful with these variables or object goes offscreen
        isSolid=True # toggle solid or outline
        showoutline=True # can show outline even if solid
        cf=b.getRGBfactors() # color list 
        color=cf['brightyellow'] # color of solid
        outlinecolor=10 # outline color
        sd=b.getshapesidedict() # common shape dict for surface definitions
        rotation=b.rotvec3D(0,20,30) # rotation vector (x,y,z) in degrees
        vertices=b.octahedravert(50) # get tetrahedra vetices
        surfaces=sd["octahedra"] # get tetrahedra surfaces
        obj3D=[vertices,surfaces] # A solid is defined by vertices and surfaces
        b.plot3Dsolid(bmp,obj3D,isSolid,color,showoutline,outlinecolor,rotation,translationvector,d,cenpt)
        b.saveBMP(file,bmp) # dump byte array to file system as-is
        print('Saved '+ file ) 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()