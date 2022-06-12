from DBNet import predict
import textre.demo
from PIL import Image
import shutil
import os
imgpath , boxes = predict.pre()
img = Image.open(imgpath)
a = 0
shutil.rmtree('D:/AI/textre/demo_image')
os.mkdir('D:/AI/textre/demo_image')
for i in range(len(boxes)-1,-1,-1):
    left = min(boxes[i][0][0],boxes[i][3][0])
    right = max(boxes[i][1][0],boxes[i][2][0])
    upper = min(boxes[i][0][1],boxes[i][1][1])
    lower = max(boxes[i][2][1],boxes[i][3][1])
    cropped = img.crop((min(left, right), min(upper, lower), max(right, left), max(lower, upper)))  # (left, upper, right, lower)
    cropped.save("D:/AI/textre/demo_image" + str(a) + ".jpg")
    a+= 1
    #cropped.show()
print(boxes)
text = textre.demo.rec()
print(text)