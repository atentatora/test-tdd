from config import *
from live_detection import paddle_ocr
import datetime
import re

def drawLine(frame):
    height, width, _ = frame.shape

    line_y = height*3//4

    start_line = (0, line_y)
    end_line = (100, line_y)

    start_line_2 = (width-100, line_y)
    end_line_2 = (width, line_y)

    frame = cv2.line(frame, start_line, end_line, (0,255,255), 2)
    frame = cv2.line(frame, start_line_2, end_line_2, (0,255,255), 2)
    
    return frame

def process_plate(frame, plate_img, x,y):
    global previous_plate
    plate_text = paddle_ocr(plate_img)
    if plate_text == "LPR01":
        return 0
    previous_plate = plate_text

    frame = drawLine(frame)
    print("Plate: ", plate_text)
    sanitized_plate = re.sub(r'[^a-zA-Z0-9]', '_', plate_text)

    if plate_text != sanitized_plate:
        print("[WARN] plate_text mismatch detected, sanitized plate: ", sanitized_plate)

    cv2.putText(frame, plate_text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    filename = f"db_caught/{sanitized_plate}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    null_plate_filename = f"db_caught/null_plate/{sanitized_plate}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    if len(plate_text) < 6:
        cv2.imwrite(null_plate_filename, frame)
        print("Saved image for PLATE ", plate_text)
    else:
        cv2.imwrite(filename, frame)
        print("Saved image for PLATE ?", plate_text)

def write_to_db():
    print("Not implemented yet.")