import cv2
  
# define a video capture object
vid = cv2.VideoCapture(0)

colors = {
    "blue":{
        "low":(84, 50, 0),
        "high": (112, 255, 255),
        "color": (255, 100, 100)
    },
    "green":{
        "low":(54, 150, 0),
        "high":(99, 255, 255),
        "color":(0, 255, 0)
    }
}

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # invert frame
    frame = cv2.flip(frame, 1)
    
    # contour each color
    for color in colors:
        masked = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), colors[color]['low'] , colors[color]['high'])
        contours, h = cv2.findContours(masked, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            contours = [x for x in contours if (x.shape[0]*x.shape[1] > 150)]
            cv2.drawContours(frame, contours, -1, colors[color]['color'], 6)

    # box for placing cube into
    for x in range(3):
        for y in range(3):
            cv2.rectangle(frame, (185+x*90, 105 + y*90), (185 + (x+1)*90, 105 + (y+1)*90), (50, 50, 50), 5)

    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()