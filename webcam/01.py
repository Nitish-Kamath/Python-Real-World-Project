import cv2  #computer vision 2
imgcapture=cv2.VideoCapture(0)  #0 ->since we have only one webcam 
result=True

while(result):
    ret,frame=imgcapture.read()  #accessing the web cam and reding the frames
    cv2.imwrite("pic.jpg",frame)
    result=False
    print("Great!! You have sucessfully captured the Image :)")
imgcapture.release()



