import numpy as np
import cv2

from time import time


def addFrame(src):
    img1 = cv2.imread(src, -1)
    img2 = cv2.imread("./frame1.png", -1)  # this one has transparency
    h, w, c = img2.shape

    img1 = cv2.resize(img1, (w, h), interpolation=cv2.INTER_CUBIC)
    result = np.zeros((h, w, 3), np.uint8)

    # slow
    # st = time()
    # for i in range(h):
    #    for j in range(w):
    #         color1 = img1[i, j]
    #         color2 = img2[i, j]
    #         alpha = color2[3] / 255.0
    #         new_color = [ (1 - alpha) * color1[0] + alpha * color2[0],
    #                       (1 - alpha) * color1[1] + alpha * color2[1],
    #                       (1 - alpha) * color1[2] + alpha * color2[2] ]
    #         result[i, j] = new_color
    # end = time() - st
    # print(end)

    # fast
    st = time()
    alpha = img2[:, :, 3] / 255.0
    result[:, :, 0] = (1. - alpha) * img1[:, :, 0] + alpha * img2[:, :, 0]
    result[:, :, 1] = (1. - alpha) * img1[:, :, 1] + alpha * img2[:, :, 1]
    result[:, :, 2] = (1. - alpha) * img1[:, :, 2] + alpha * img2[:, :, 2]
    end = time() - st
    print(end)

#     cv2.imshow("result", result)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

    return result
