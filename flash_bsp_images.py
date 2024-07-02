#!/usr/bin/python
import sys
import os

if __name__ == "__main__":
    print("********* Starting bootburn/flash_bsp_images.py *********")

    scriptDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.join(scriptDir,os.pardir)
    sys.path.append(parentDir)

    flashPath = os.path.join(scriptDir, "..", "..","..","tools", "flashtools")
    isPdkPackage = os.path.isdir(flashPath)

    DISABLE_BOOTBURN_T23X = False
    if DISABLE_BOOTBURN_T23X or ('-b' in sys.argv and 't194' in sys.argv[sys.argv.index('-b')+1]) :
        if isPdkPackage:
            sys.path.insert(0, os.path.join(parentDir, "bootburn_t19x_py"))
            from bootburn_t19x_py.flash_bsp_images import flash_bsp
        else:
            sys.path.insert(0, os.path.join(parentDir, "t194_bootburn_py"))
            from t194_bootburn_py.flash_bsp_images import flash_bsp
    else:
        if isPdkPackage:
            sys.path.insert(0, os.path.join(parentDir, "bootburn_t23x_py"))
            from bootburn_t23x_py.flash_bsp_images import flash_bsp
        else:
            sys.path.insert(0, os.path.join(parentDir, "t23x_bootburn_py"))
            from t23x_bootburn_py.flash_bsp_images import flash_bsp

    result = flash_bsp(sys.argv)
    sys.exit(result)
