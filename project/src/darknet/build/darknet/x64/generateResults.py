import os
if __name__ == '__main__':
    for i in range(53):
        os.system("darknet.exe detector map data/obj.data yolo-obj.cfg backup\yolo-obj_{}.weights > results/mapResults_{}.txt".format((i+1)*100,(i+1)*100))
        os.system("darknet.exe detector test data/obj.data yolo-obj.cfg backup/yolo-obj_{}.weights -dont_show -ext_output < data/train.txt > results/result_{}.txt".format((i+1)* 100, (i+1)*100))
