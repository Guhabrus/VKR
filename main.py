from itertools import count
import cv2
import os
import shutil


PATH = "/home/maksim/Myfolder/Magistr/VKR/image/Validate/"
Ver = "F6_"

def get_group():
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            
            # os.rename(PATH +filename, PATH + "A4_"+filename)
            shutil.move(PATH +filename, "/home/maksim/Myfolder/Magistr/VKR/image/" + Ver+filename)
            print("/home/maksim/Myfolder/Magistr/VKR/image/" + Ver+filename)
           
        break 


def work():
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            print(PATH +filename)
            if(PATH +filename == "/home/maksim/Myfolder/Magistr/VKR/image/main.py"):
                continue
            
            image = cv2.imread(PATH +filename)   

            cv2.imshow("Original image", image)
            
            key = cv2.waitKey(0) 
            if key == ord('n'):
                os.replace(PATH+filename, PATH+"Validate/"+filename)
                continue    
            elif key == ord('d'):
                os.remove(PATH +filename)
            elif key == ord('q'):
                break
        # break
            

def rename():
    count = 1
    for root, dirs, files in os.walk(PATH):
            for filename in files:
                print(PATH +filename)
                os.rename(PATH+filename, PATH + str(count) + ".png")
                count+=1
               
            

# work()
# get_group()

rename()