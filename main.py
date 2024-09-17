import cv2 as cv
from time import time, sleep
import pyautogui as gui
from ultralytics import YOLO

model = YOLO("best.pt")
text_height = 100
current_time = 0
counter_start = 0
counter_end = 0
last_prediction_time = 0
x_player1 = True

def draw_grid(frame) :
   
    width = frame.shape[1]
    height = frame.shape[0] - text_height
    cv.line(
        frame,
        (int(width / 3), text_height),
        (int(width / 3), height + text_height),
        (200, 255, 100),
        thickness=3,
    )
    cv.line(
        frame,
        (int((2 * width) / 3), text_height),
        (int((2 * width) / 3), height + text_height),
        (200, 255, 100),
        thickness=3,
    )
    cv.line(frame, (0, text_height), (width, text_height), (200, 0, 100), thickness=3)
    cv.line(
        frame,
        (0, int(height / 3) + text_height),
        (width, int(height / 3) + text_height),
        (200, 255, 100),
        thickness=3,
    )
    cv.line(
        frame,
        (0, int((2 * height) / 3) + text_height),
        (width, int((2 * height) / 3) + text_height),
        (200, 255, 100),
        thickness=3,
    )
def draw_o(frame, center_x, center_y, player):
    global pin
    global box_width
    global box_height
    for row in pin:
        for box in row:
            if (center_x <= (box[0] + (box_width / 2))) and (center_x >= (box[0] - (box_width / 2))):
                if (center_y <= (box[1] + (box_height / 2))) and (center_y >= (box[1] - (box_height / 2))) and (not player):
                    if box[2] != 1:
                        box[2] = 2
            if box[2] == 2:
                cv.circle(frame, (box[0],box[1]), 50, (255,200,0), thickness=3)
    win_check()


def draw_x(frame, center_x, center_y, player):
    global pin
    size = 70
    for row in pin:
        for box in row:
            if (center_x <= (box[0] + (box_width / 2))) and (center_x >= (box[0] - (box_width / 2))):
                if (center_y <= (box[1] + (box_height / 2))) and (center_y >= (box[1] - (box_height / 2))) and player:
                    if box[2] != 2:
                        box[2] = 1
            if box[2] == 1:
                top_left = (box[0] - size // 2, box[1] - size // 2)
                bottom_right = (box[0] + size // 2, box[1] + size // 2)

                top_right = (box[0] + size // 2, box[1] - size // 2)
                bottom_left = (box[0] - size // 2, box[1] + size // 2)

                cv.line(frame, top_left, bottom_right, (0,200,255), thickness=4)
                cv.line(frame, top_right, bottom_left, (0,200,255), thickness=4)
    win_check()

def print_text(frame, text):
    cv.putText(frame, text, (400,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)

def print_timer(frame, start):
    global current_time
    current_time = int(time()) - start
    cv.putText(frame, f"{current_time}",(50,50), cv.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)
    return frame, start

def count_down(frame):
    global current_time, counter_start, counter_end
    if counter_start == 0:
        counter_start = current_time
        counter_end = counter_start + 2
        return False
    if (current_time) >= counter_end:
        counter_start = 0
        return True
    else:
        to_print = counter_end - int(time())
        #print_text(frame, f"{to_print}")
        return False


def set_turn():
    global x_player1
    if x_player1:
        x_player1 = False
    else:
        x_player1 = True

def get_turn():
    global x_player1, flipped_frame
    if not x_player1:
        cv.putText(flipped_frame, "O Player's Turn..", (200,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
    else:
        cv.putText(flipped_frame, "X Player's Turn..", (200,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)

def end(player):
    if player == 2:
        cv.putText(flipped_frame, "O Player's Turn..", (200,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
    else:
        cv.putText(flipped_frame, "X Player's Turn..", (200,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
    sleep(2)
    cap.release()
    cv.destroyAllWindows()

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
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

frame_width = 640
frame_height = 640
cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)

# define boxes and adjust positions
box_width = frame_width // 3
box_height = frame_height // 3
top_left = [int(box_width / 2), int(box_height / 2) + text_height,0]
top_center = [int(box_width * 3 / 2), int(box_height / 2) + text_height, 0]
top_right = [int(box_width * 5 / 2), int(box_height / 2) + text_height, 0]
middle_left = [int(box_width / 2), int(box_height * 3 / 2) + text_height //2, 0]
middle_center = [int(box_width * 3 / 2), int(box_height * 3 / 2) + text_height //2, 0]
middle_right = [int(box_width * 5 / 2), int(box_height * 3 / 2) + text_height //2, 0]
bottom_left = [int(box_width / 2), int(box_height * 5 / 2) + text_height-50, 0]
bottom_center = [int(box_width * 3 / 2), int(box_height * 5 / 2) + text_height-50, 0]
bottom_right = [int(box_width * 5 / 2), int(box_height * 5 / 2) + text_height-50, 0]
pin = [
    [top_left, top_center, top_right],
    [middle_left, middle_center, middle_right],
    [bottom_left, bottom_center, bottom_right]
]

def predict():
            results = model.predict(
            source=raw_flipped_frame, save=True, imgsz=640, conf=0.8
            )
            boxes_num = len(results[0].boxes)
            if boxes_num == 0:
                return -1,-1, True
            #print (boxes_num)
            for r in results:
                    coordinates=r.boxes.xywh.cpu().numpy()
                    classes_label=r.boxes.cls.cpu().numpy()
                    i = 0
                    # Attention Please! the following block of code returns the following:
                    # name of the box in variable name
                    # x_center of the box in variable x_center
                    # y_center of the box in variable y_center
                    while i < boxes_num :
                            id = classes_label[i]
                            name = model.names[id]
                            x_center = coordinates[i][0]
                            y_center = coordinates[i][1]
                            i+=1
                            #write after this line directly the logic to be done as the following pseudo code and do not write after the dots
                            if name == 'x' and x_player1:
                                set_turn()
                                return int(x_center), int(y_center), True
                            elif name == 'o'and (not x_player1):
                                set_turn()
                                return int(x_center), int(y_center), False
                            else :
                                return -1, -1, True
                            
                            
start = int(time())

while True:
    isTrue, frame = cap.read() #read the frames from the video
    if isTrue and frame is not None: # if there is a frame
        frame = cv.resize(frame, (640, 640))  # Ensure the frame is resized to 640x640
        flipped_frame = cv.flip(frame, 1)  # Flip frame for display only
        raw_flipped_frame = flipped_frame.copy() # used by model without any drawing
        draw_grid(flipped_frame)
        flipped_frame, start = print_timer(flipped_frame, start)
        x = -1
        y = -1
        player = True
        condition = count_down(flipped_frame)
        get_turn()
        if condition:
            x, y, player = predict()
        draw_x(flipped_frame,x,y, player)
        draw_o(flipped_frame,x,y, player)

                            
        cv.imshow("video",flipped_frame)

    if cv.waitKey(20) & 0xFF==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()

