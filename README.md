# Python_BMP
A pure Python 2D/3D graphics library that outputs to windows bitmap format

>Developed and tested using Python 3.7.3
>No dependencies required

# Instructions

Run Hello_somestring_here.py
>This will show minimum code to accomplish certain tasks
>Hello_Darkness.py my old friend is minimum template 

Run Features_Speedtest.py 

>It should generate a bitmap and open MS Paint under windows to show output... 
>Close the MS Paint window to execute another script

under unix change editor at line 168 (see below)

>ret =proc.call('mspaint '+file) # replace with another editor if Unix
>or comment the line 

You can inspect the file later with another graphics editor file name is

>file='test.bmp' 
>at line 162

# Unit tests

Run picmanip_UNITTEST.py 

>it will generate up to 70+ images (one per function under test) then compare it with previously generated images generated with the function under test 
>(this might take a while)




