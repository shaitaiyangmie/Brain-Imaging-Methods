import cv2.cv2 as cv2


def img_cut(root):
    img_dir = root
    img = cv2.imread(img_dir)
    bbox = cv2.selectROI(img, False)
    cut = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
    cv2.imwrite('/Users/shaotianyu01/Desktop/school/img_pred/cut.jpg', cut)
    # cv2.imwrite('/Users/shaotianyu01/Desktop/school/img_pred/cut_{}.jpg'.format(name), cut)
