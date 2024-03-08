username = '[REDACTED]'
password = '[REDACTED]'
ip = '192.168.1.64'

import cv2
import numpy as np
import paddleocr
import sqlite3

ocrp = paddleocr.PaddleOCR(show_log=False, use_angle_cls=True, lang='en')
stream = cv2.VideoCapture(f'rtsp://{username}:{password}@{ip}/')
plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

whitelist_db = sqlite3.connect('anpr_wl.db')
history_db = sqlite3.connect('anpr_history.db')