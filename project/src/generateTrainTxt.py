# Data Preperation File
# -*- coding: utf-8 -*-
import os

SOURCE_DIR = "../../annotations"
DARKNET_ADJUSTMENT = "../../../.."

TARGET_FILE = "train.txt"

if __name__ == '__main__':
    if(not os.path.isdir(SOURCE_DIR)):
        print("NO SOURCE DIRECTORY FOUND WITH NAME: {}".format(SOURCE_DIR))

    with open(TARGET_FILE, "w") as results:
        for i, fname in enumerate(os.listdir(SOURCE_DIR), 1):
            ext = fname.strip().split(".")[-1]
            if(ext == "jpg"):
                results.write("{}/{}/{}\n".format(DARKNET_ADJUSTMENT, SOURCE_DIR, fname))

    print("PROCESSING COMPLETE: {} IMAGES FOUND".format(i))
