import os
from PIL import ImageGrab, Image
import numpy as np

pre = np.array(ImageGrab.grab())
h = len(pre)
w = len(pre[0])

i = ImageGrab.grab()
box = (21,73,186,231)
i =  i.crop(box)
np.array(i)
for f in os.listdir("character portraits"):
    img = Image.open("character portraits/"+f)
    