import os
import cv2
path = "Images/"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)               
        images.append(file_name)

frame = cv2.imread(images[0])  
height,width,channels= frame.shape 
print(len(images))
count = len(images)
size = (width, height)
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(count):
    frame = cv2.imread(images[i])
    out.write(frame)
    cv2.waitKey(1)  
out.release()
print("Done")