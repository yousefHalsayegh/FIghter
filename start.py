import cv2 
from PIL import ImageGrab
import numpy as np

pre = np.array(ImageGrab.grab())
h = len(pre)
w = len(pre[0])

while True:
    img = np.array(ImageGrab.grab())
    
    img = cv2.line(img, (round(w*0.5),0), (round(w*0.5), h), (0,200,0), 20)
    img = cv2.line(img, (round(w*0.25),h//2), (round(w*0.75), h//2), (0,200,0), 20)
    imgShow = cv2.resize(img, (1000,1000))
    cv2.imshow("cam", cv2.cvtColor(imgShow, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()