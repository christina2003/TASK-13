import cv2 as cv
from time import time
import pyautogui as gui

text_height = 100
current_time = 0
counter_start = 0
counter_end = 0

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
    win_check()

def draw_x(frame, center_x, center_y):
    size = 70
    top_left = (center_x - size // 2, center_y - size // 2)
    bottom_right = (center_x + size // 2, center_y + size // 2)
    
    top_right = (center_x + size // 2, center_y - size // 2)
    bottom_left = (center_x - size // 2, center_y + size // 2)

    cv.line(frame, top_left, bottom_right, (255,200,0), thickness=4)
    cv.line(frame, top_right, bottom_left, (255,200,0), thickness=4)
    win_check()

def print_text(frame, text):
    cv.putText(frame, text, (300,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,50,100), 2)

def print_timer(frame, start):
    global current_time
    current_time = int(time()) - start
    cv.putText(frame, f"{current_time}",(50,50), cv.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
    return frame, start

def count_down(frame):
    global current_time, counter_start, counter_end
    if counter_start == 0:
        counter_start = current_time
        counter_end = counter_start + 5
        return False
    if time() >= counter_end:
        print("continue here")
        #take input from model
        counter_start = 0
        return True
    else:
        print_text(frame, f"{counter_end - time()}")
        return False


def turn(frame, Is_player1):
    if Is_player1:
        print_text(frame, f"Player1, GET READY!")
        condition = count_down(frame)
    else:
        print_text(frame, f"Player2, GET READY!")
        condition = count_down(frame)
    if condition:
        return not(Is_player1)
    else:
        return Is_player1

def end(player):
    if player:
        print_text("player 2 wins!")
    else:
        print_text("player 1 wins!")

def win_check():
    for i in range(3):
        if pin[i][0][2] == pin[i][1][2] == pin[i][2][2] != 0:
            end(pin[i][0][2])
            break
        elif pin[0][i][2] == pin[1][i][2] == pin[2][i][2] != 0:
            end(pin[0][i][2])
            break
    else:
        if pin[0][0][2] == pin[1][1][2] == pin[2][2][2] != 0:
            end(pin[1][1][2])
        elif pin[2][0][2] == pin[1][1][2] == pin[0][2][2] != 0:
            end(pin[1][1][2])

cap = cv.VideoCapture(0) 
isTrue, frame = cap.read()
frame_width, frame_height = gui.size()
# change the ration
cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)

# define boxes
box_width = frame_width // 3
box_height = frame_height // 3
top_left = [int(box_width / 2), int(box_height / 2) + text_height,0]
top_center = [int(box_width * 3 / 2), int(box_height / 2) + text_height, 0]
top_right = [int(box_width * 5 / 2), int(box_height / 2) + text_height, 0]
middle_left = [int(box_width / 2), int(box_height * 3 / 2) + text_height //2, 0]
middle_center = [int(box_width * 3 / 2), int(box_height * 3 / 2) + text_height //2, 0]
middle_right = [int(box_width * 5 / 2), int(box_height * 3 / 2) + text_height //2, 0]
bottom_left = [int(box_width / 2), int(box_height * 5 / 2) + text_height, 0]
bottom_center = [int(box_width * 3 / 2), int(box_height * 5 / 2) + text_height, 0]
bottom_right = [int(box_width * 5 / 2), int(box_height * 5 / 2) + text_height, 0]
pin = [
    [top_left, top_center, top_right],
    [middle_left, middle_center, middle_left],
    [bottom_left, bottom_center, bottom_right]
]
start = int(time())
Is_player1 = True
while True:
    isTrue, frame = cap.read() #read the frames from the video
    if isTrue: # if there is a frame

        draw_grid(frame)
        # testing the functions
        draw_o(frame,top_right[0],top_right[1])
        draw_x(frame, bottom_center[0], bottom_center[1])
        frame, start = print_timer(cv.flip(frame,1), start)

        # game logic is here
        Is_player1 = turn(frame, Is_player1)
        # display the video
        cv.imshow("video",frame)

    if cv.waitKey(20) & 0xff==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()

