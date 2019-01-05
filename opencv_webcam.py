# import cv2

# def webcam():
# 	try:
# 		print('start')
# 		cap=cv2.VideoCapture(0)
# 	except:
# 		print('fail')
# 		return
# 	cap.set(3,480)
# 	cap.set(4,320)

# 	while True:
# 		ret,frame=cap.read()

# 		if not ret:
# 			print('error')
# 			break

# 		video=cv2.cvtColor(frame,COLOR_BGR2GRAY)
# 		cv2.imshow('video',video)

# 		k=cv2.waitkey(1) & 0xFF
# 		if k==27: #esc
# 			break

# 		cap.release()
# 		cv2.destroyAllWindows()

# webcam()

import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()