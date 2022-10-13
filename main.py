import cv2
  
# define a video capture object
vid = cv2.VideoCapture(0)

# white = (255, 255, 255)
# white = cv2.COLOR_RGB2HSV((255, 255, 255))
black = (0, 0, 0)

colors = {
    "blue":{
        "low":(103, 139, 0),
        "high": (120, 243, 255),
        "color": (255, 0, 0)
    },
    "green":{
        "low":(43, 130, 0),
        "high":(93, 255, 255),
        "color":(0, 255, 0)
    }
}

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # invert frame
    frame = cv2.flip(frame, 1)
    
    for color in colors:
        masked = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), colors[color]['low'] , colors[color]['high'])
        contours, h = cv2.findContours(masked, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours[], -1, colors[color]['color'], 6)

    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()