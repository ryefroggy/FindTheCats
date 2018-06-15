import subprocess
import os

WEIGHTS_DIR = ".\darknet\\build\darknet\\x64\\backup\\"
EXE = ".\darknet\\build\darknet\\x64\darknet.exe"

TARGET_FILE = "train.txt"

if __name__ == '__main__':
    if(not os.path.isdir(WEIGHTS_DIR)):
        print("NO WEIGHTS DIRECTORY FOUND")

    with open(TARGET_FILE, "w") as results:
        for i, fname in enumerate(os.listdir(WEIGHTS_DIR), 1):
            result = subprocess.run([EXE, "detector", "map", "data/obj.data", "yolo-obj.config", "backup\\" + fname], stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))
    ### For after processing the last line of each std out from processing each set of weights. Each set of weights gets 1 point. This will be the mAP value.
    #savefig("graph.jpg")
    print("PROCESSING COMPLETE")