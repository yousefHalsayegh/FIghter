import os
from PIL import ImageGrab, Image
import numpy as np




i = ImageGrab.grab()
box = (21,73,186,231)
i =  i.crop(box)
i.save("crop.png")
player_1 = np.array(i)
for f in os.listdir("character portraits"):
    img = np.array(Image.open("character portraits/"+f))
    y_por = len(img)//2
    x_por = len(img[0])//2
    print(f'For {f}, on ({y_por}, {x_por}) the color is {img[y_por][x_por]}')



