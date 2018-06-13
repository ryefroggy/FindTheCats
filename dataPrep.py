# Data Preperation File
# -*- coding: utf-8 -*-
import os
import PIL.Image, PIL.ImageTk

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except (AttributeError, OSError):
    ctypes.windll.user32.SetProcessDPIAware()

RESULT_SIZE = (320, 320)
SOURCE_DIR = "downloads"

RESULT_DIR = "processedData"

absImageCount = 0

def getOptimalSize(width, height):
    ratio = min(RESULT_SIZE[0]/width, RESULT_SIZE[1]/height)
    return (int(width * ratio), int(height * ratio))

def processDir(tDir, progressMarkers = 20):
    global absImageCount

    for count, entry in enumerate(os.listdir(tDir), 1):
        fpath = "{}/{}".format(tDir, entry)
        if(not os.path.isfile(fpath)):
            continue

        absImageCount += 1
        rpath = "{}/{}.jpg".format(RESULT_DIR, "%05d" % absImageCount)
        template = PIL.Image.new("RGB", RESULT_SIZE, (0, 0, 0))

        try:
            im = PIL.Image.open(fpath)
            newdims = getOptimalSize(im.size[0], im.size[1])
            im = im.resize(newdims, PIL.Image.ANTIALIAS)

            template.paste(im, (0, 0))

            template.save(rpath, "JPEG")
            print("IMAGE CREATED: {}".format(rpath))
        except Exception as e:
            print("FAILED TO CREATE IMAGE FOR IMAGE: {}".format(fpath))
            print("ERROR INFO: {}".format(e))

        if(count % progressMarkers == 0):
            print("PROGRESS MARKER {}".format(count))

    return count

if __name__ == '__main__':
    if(not os.path.isdir(SOURCE_DIR)):
        print("NO SOURCE DIRECTORY FOUND WITH NAME: {}".format(SOURCE_DIR))
    if(not os.path.isdir(RESULT_DIR)):
        print("OUTPUT DIRECTORY MADE: {}".format(RESULT_DIR))
        os.makedirs(RESULT_DIR)

    for subdir in os.listdir(SOURCE_DIR):
        subpath = "{}/{}".format(SOURCE_DIR, subdir)
        print("{} :: {}".format(subpath, os.path.isdir(subpath)))

        processedCount = processDir(subpath)
        print("IMAGES FOUND: {}".format(processedCount))

    print("PROCESSING COMPLETE: {} IMAGES SUCCEEDED".format(absImageCount))
