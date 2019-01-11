import cv2
import numpy as np
import sys


def main():
    if len(sys.argv) == 1 or sys.argv[1][-3:-1] + sys.argv[1][-1] != "bmp":
        print("require a bmp file")
        return
    filename = sys.argv[1]
    bmp = cv2.imread(filename, 0)
    row, col = bmp.shape
    bmp_inverse = np.zeros_like(bmp)
    for r in range(row):
        for l in range(col):
            bmp_inverse[r, l] = 255 - bmp[r, l]
    cv2.imwrite(filename[:-4] + "_inverse_black_white.bmp", bmp_inverse)


if __name__ == '__main__':
    main()

