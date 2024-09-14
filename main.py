import cv2 as cv


def draw_grid(frame) :
    width = frame.shape[1]
    height = frame.shape[0]
    # draw virtical lines
    cv.line(frame, (int(width/3),0),(int(width/3),height),(200,255,100),thickness=3) # draw a line (img, point1, point2, color,thickness=5)
    cv.line(frame, (int((2 * width)/3),0),(int((2 * width)/3),height),(200,255,100),thickness=3) 
    # draw Horizontal line
    cv.line(frame, (0,int(height/3)),(width,int(height/3)),(200,255,100),thickness=3) # draw a line (img, point1, point2, color,thickness=5)
    cv.line(frame, (0,int((2 * height)/3)),(width,int((2 * height)/3)),(200,255,100),thickness=3)

def draw_o(frame, center_x, center_y):
    cv.circle(frame, (center_x,center_y), 50, (255,200,0), thickness=3)

def draw_x(frame, center_x, center_y):
    size = 70
    top_left = (center_x - size // 2, center_y - size // 2)
    bottom_right = (center_x + size // 2, center_y + size // 2)
    
    top_right = (center_x + size // 2, center_y - size // 2)
    bottom_left = (center_x - size // 2, center_y + size // 2)

    cv.line(frame, top_left, bottom_right, (255,200,0), thickness=4)
    cv.line(frame, top_right, bottom_left, (255,200,0), thickness=4)

cap = cv.VideoCapture(0) 
while True:
    isTrue, frame = cap.read() #read the frames from the video

    # define boxes
    box_width = frame.shape[1] // 3
    box_height = frame.shape[0] // 3

    top_left       = [int(box_width / 2), int(box_height / 2)]
    top_center     = [int(box_width * 3 / 2), int(box_height / 2)]
    top_right      = [int(box_width * 5 / 2), int(box_height / 2)]

    middle_left    = [int(box_width / 2), int(box_height * 3 / 2)]
    middle_center  = [int(box_width * 3 / 2), int(box_height * 3 / 2)]
    middle_right   = [int(box_width * 5 / 2), int(box_height * 3 / 2)]

    bottom_left    = [int(box_width / 2), int(box_height * 5 / 2)]
    bottom_center  = [int(box_width * 3 / 2), int(box_height * 5 / 2)]
    bottom_right   = [int(box_width * 5 / 2), int(box_height * 5 / 2)]

    if isTrue: # if there is a frame

        draw_grid(frame)
        # testing the functions
        draw_o(frame,top_right[0],top_right[1])
        draw_x(frame, bottom_center[0], bottom_center[1])

        # game logic is here 

        # display the video
        cv.imshow("video", frame)

    if cv.waitKey(20) & 0xff==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()

