import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    """function to rescale the frames"""
    width = int(frame.shape[1] * scale)
    hight = int(frame.shape[0] * scale)

    dimentions = (width, hight)
    # cv.resize(img, (200, 200))
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)


cap = cv.VideoCapture("data.mp4") # get video path
count = 0
while True:
    isTrue, frame = cap.read() #read the frames from the video

    if isTrue: # if there is a frame
        frame = rescaleFrame(frame, scale = 0.25)
        cv.imwrite(f"data/quarter_scale/output_{count}.png", frame) # save the output img
        count += 1

    if cv.waitKey(20) & 0xff==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()