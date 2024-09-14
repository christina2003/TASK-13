import cv2 as cv

text_height = 100

def draw_grid(frame) :
   
    width = frame.shape[1] 
    height = frame.shape[0] - text_height
    # draw virtical lines
    cv.line(frame, (int(width/3),text_height),(int(width/3),height+text_height),(200,255,100),thickness=3) # draw a line (img, point1, point2, color,thickness=5)
    cv.line(frame, (int((2 * width)/3),text_height),(int((2 * width)/3),height+text_height),(200,255,100),thickness=3) 
    # draw Horizontal line
    cv.line(frame, (0,text_height),(width,text_height),(200,0,100),thickness=3)
    cv.line(frame, (0,int(height/3) +text_height),(width,int(height/3)+text_height),(200,255,100),thickness=3) # draw a line (img, point1, point2, color,thickness=5)
    cv.line(frame, (0,int((2 * height)/3)+text_height),(width,int((2 * height)/3)+text_height),(200,255,100),thickness=3)

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

def show_text(frame, text):
    cv.putText(frame, text, (50,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,50,100), 2)



cap = cv.VideoCapture(0)
# frame dimention
frame_width = 1280
frame_height = 720

# change the ration
cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)

 # define boxes
box_width = (frame_width // 3)
box_height = (frame_height // 3)

top_left       = [int(box_width / 2), int(box_height / 2) +text_height]
top_center     = [int(box_width * 3 / 2), int(box_height / 2)+text_height]
top_right      = [int(box_width * 5 / 2), int(box_height / 2)+text_height]

middle_left    = [int(box_width / 2), int(box_height * 3 / 2)+text_height//2]
middle_center  = [int(box_width * 3 / 2), int(box_height * 3 / 2)+text_height//2]
middle_right   = [int(box_width * 5 / 2), int(box_height * 3 / 2)+text_height//2]

bottom_left    = [int(box_width / 2), int(box_height * 5 / 2)]
bottom_center  = [int(box_width * 3 / 2), int(box_height * 5 / 2)]
bottom_right   = [int(box_width * 5 / 2), int(box_height * 5 / 2)]


while True:
    isTrue, frame = cap.read() #read the frames from the video

   
    if isTrue: # if there is a frame

        draw_grid(frame)
        show_text(frame, "Ready for the Game !!")
        # testing the functions
        draw_o(frame,top_left[0],top_left[1])
        draw_o(frame,top_center[0],top_center[1])
        draw_o(frame,top_right[0],top_right[1])

        draw_x(frame, bottom_center[0], bottom_center[1])
        draw_x(frame, bottom_left[0], bottom_left[1])
        draw_x(frame, bottom_right[0], bottom_right[1])

        draw_x(frame, middle_center[0], middle_center[1])
        draw_x(frame, middle_left[0], middle_left[1])
        draw_x(frame, middle_right[0], middle_right[1])

        # game logic is here 
        # 

        # display the video
        cv.imshow("video", frame)

    if cv.waitKey(20) & 0xff==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()

