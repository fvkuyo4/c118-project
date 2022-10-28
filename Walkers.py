import cv2


# Create our body classifier
import cv2

facecascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    grey = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    # Pass frame to our body 
    faces = facecascade.detectMultiScale(grey)
    
    # Extract bounding boxes for any bodies identified
    for(x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #crop the image to save the face image
    #roi stands for region of interest
   
     cv2.imshow("image",frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
