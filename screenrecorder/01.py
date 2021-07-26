import cv2
import numpy as np   #numpy ->it is module for importing array
from  PIL import ImageGrab

#Basic logic behind screenbrecording is ,it capture the screen frame by frame


def screenRecorder():
    fourcc =cv2.VideoWriter_fourcc(*'XVID')      #fourcc ->four character code
    out=cv2.VideoWriter("output.avi",fourcc,5.0,(1920,1080)) #out->output  5.0-> it is the frame at which screen is being captured
    

    while True:
        img= ImageGrab.grab()
        img_np=np.array(img)                                   #converting image into numpy array
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)            #cvt->convert  BGR->blue green red to RGB->red green blue
        
        cv2.imshow("Screen Recorder",frame)
        out.write(frame)


        if cv2.waitKey(1) == 27:   #port for  q key on the keybaord
            break

    out.release()
    cv2.destroyAllWindows()
screenRecorder()
