#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

def enumletters(st:str) -> str:
    c,i=len(st),0
    while i<c:
        yield st[i:i+1]
        i+=1

def enumreverseletters(st:str) -> str:
    i=len(st)-1
    while i>-1:
        yield st[i:i+1]
        i-=1

def char2int(charcodestr:str) -> int:
    place,strhash=0,0
    for c in enumletters(charcodestr):
        strhash=strhash+ord(c)*(256**place)
        place+=1
    return strhash