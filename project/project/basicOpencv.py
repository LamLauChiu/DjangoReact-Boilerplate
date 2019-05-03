import numpy as np
import cv2
from matplotlib import pyplot as plt


# sources: https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/
# 讀取圖檔
img = cv2.imread('/Users/Ivan.lam/Projects/DjangoReact-Boilerplate/project/project/human-20180303-01-1024x683.jpg')

# 查看資料型態
#type(img)

#img.shape

# 以灰階的方式讀取圖檔
#img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 顯示圖片
#cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# 關閉 'My Image' 視窗
#cv2.destroyWindow('My Image')


# 讓視窗可以自由縮放大小
#cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)

#cv2.imshow('My Image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# 寫入圖檔
#cv2.imwrite('output.jpg', img)
# 寫入不同圖檔格式
#cv2.imwrite('output.png', img)
#cv2.imwrite('output.tiff', img)

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
#cv2.imwrite('output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
#cv2.imwrite('output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])


# 使用 OpenCV 讀取圖檔
#img_bgr = cv2.imread('/Users/Ivan.lam/Projects/DjangoReact-Boilerplate/project/project/human-20180303-01-1024x683.jpg')

# 將 BGR 圖片轉為 RGB 圖片
#img_rgb = img_bgr[:,:,::-1]

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
#plt.imshow(img_rgb)
#plt.show()


# 使用 OpenCV 讀取灰階圖檔
img_gray = cv2.imread('/Users/Ivan.lam/Projects/DjangoReact-Boilerplate/project/project/human-20180303-01-1024x683.jpg', cv2.IMREAD_GRAYSCALE)

# 使用 Matplotlib 顯示圖片
plt.imshow(img_gray, cmap = 'gray')
plt.show()
