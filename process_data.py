from config import *
from live_detection import paddle_ocr
import datetime
import re

def drawLine(coke):
    height, width, _ = coke.shape

    line_y = height*3//4

    start_line = (0, line_y)
    end_line = (100, line_y)

    start_line_2 = (width-100, line_y)
    end_line_2 = (width, line_y)

    coke = cv2.line(coke, start_line, end_line, (0,255,255), 2)
    coke = cv2.line(coke, start_line_2, end_line_2, (0,255,255), 2)
    
    return coke

def process_plate(frame, plate_img, x,y):
    global previous_plate
    plate_text = paddle_ocr(plate_img)
    if plate_text == "LPR01":
        return 0
    previous_plate = plate_text

    frame = drawLine(frame)
    print("Plate: ", plate_text)

    cv2.putText(frame, plate_text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    filename = f"db_caught/{plate_text}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    cv2.imwrite(filename, frame)

def write_to_db():
    print("Not implemented yet.")