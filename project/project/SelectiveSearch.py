'''

source :https://blog.gtwang.org/programming/selective-search-for-object-detection/

explore: http://www.huppelen.nl/publications/selectiveSearchDraft.pdf

初版的 R-CNN 是將 Selective Search 所得到的候選區域，放進 CNN 中進行判斷，為了更清楚理解 Selective Search 的運作，
以下我們直接使用 OpenCV 來撰寫一個 Selective Search 的實作版本，觀察該演算法實際執行的結果。

Selective Search 理論

Selective Search 的理論概念就是使用圖像分割（segmentation）後的結果，
套用階層群聚演算法（hierarchical grouping algorithm），產生物體的候選區域（object proposal），最後再用 SVM 辨識物體。
'''

import cv2

# 讀取圖檔
im = cv2.imread('/Users/Ivan.lam/Projects/DjangoReact-Boilerplate/project/project/human-20180303-01-1024x683.jpg')

# 建立 Selective Search 分割器
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

# 設定要進行分割的圖形
ss.setBaseImage(im)

# 使用快速模式（精準度較差）
ss.switchToSelectiveSearchFast()

# 使用精準模式（速度較慢）
# ss.switchToSelectiveSearchQuality()

# 執行 Selective Search 分割
rects = ss.process()

print('候選區域總數量： {}'.format(len(rects)))

# 要顯示的候選區域數量
numShowRects = 100

# 每次增加或減少顯示的候選區域數量
increment = 50

while True:
  # 複製一份原始影像
  imOut = im.copy()

  # 以迴圈處理每一個候選區域
  for i, rect in enumerate(rects):
      # 以方框標示候選區域
      if (i < numShowRects):
          x, y, w, h = rect
          cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
      else:
          break

  # 顯示結果
  cv2.imshow("Output", imOut)

  # 讀取使用者所按下的鍵
  k = cv2.waitKey(0) & 0xFF

  # 若按下 m 鍵，則增加 numShowRects
  if k == 109:
      numShowRects += increment
  # 若按下 l 鍵，則減少 numShowRects
  elif k == 108 and numShowRects > increment:
      numShowRects -= increment
  # 若按下 q 鍵，則離開
  elif k == 113:
      break

# 關閉圖形顯示視窗
cv2.destroyAllWindows()