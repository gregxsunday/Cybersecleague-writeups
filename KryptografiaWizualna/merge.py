import cv2


def blend(img1, img2, no1, no2):
    dst = cv2.addWeighted(img1,0.5,img2,0.5, 0)
    outputname = str(no1) + '-' + str(no2)
    cv2.imshow(outputname,dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


for i in range(1, 11):
    for j in range(1,11):
        blend(cv2.imread('img\\' + str(i) + '.png'), cv2.imread('img\\' + str(j) + '.png'), i, j)