notice = """
 Documentation Generator Py Version
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
 Output to %s
"""
from Python_BMP.BITMAPlib import(
        getfuncmetastr as meta,
        )

from inspect import getmembers, isfunction
import Python_BMP.BITMAPlib as m

import subprocess as proc
from os import path


def savelist(mlist: list, filename: str):
    with open(filename,'w') as f:
        for m in mlist:
            f.write(f'{m}\n\n')
        f.close()


def main():
        edt = 'notepad' # change if Linux
        file = 'BitmapLib_Doc.py'
        print(f'{notice % (file)}')
        savelist([meta(m[1]) for m in getmembers(m, isfunction)], file)
        ret = proc.call([edt, file])

if __name__=="__main__":
        main()

