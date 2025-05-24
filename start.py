import cv2 
from PIL import ImageGrab
import numpy as np
import easyocr
import time

pre = np.array(ImageGrab.grab())
h = len(pre)
w = len(pre[0])

reader = easyocr.Reader(['en'], gpu=False)

def drawing (f,r):   
       
    f = cv2.line(f, (round(w*0.5),0), (round(w*0.5), h), (0,255,0), 20)
    f = cv2.line(f, (round(w*0.25),h//2), (round(w*0.75), h//2), (0,255,0), 20)
    for r_ in r:
        p, t, x = r_
        f = cv2.rectangle(f, p[0], p[2], (0,255,0), 5)
        f = cv2.putText(f, t.lower(), p[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
    return f

count = 0 
while True:

    img = np.array(ImageGrab.grab())

    if count <= 1:
        text = reader.readtext(img)
        img = drawing(img, text)
        

   
    

        imgShow = cv2.resize(img, (1000,1000))
        cv2.imshow("cam", cv2.cvtColor(imgShow, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(1) == ord('q'):
        break
    count += 1


cv2.destroyAllWindows()