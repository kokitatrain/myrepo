import cv2
import os 
video_path = 'viddata.mp4'
destination_folder = 'regler'

os.makedirs(destination_folder, exist_ok=True)
video = cv2.VideoCapture(video_path)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

size = (640, 640)
frame_rate =video.get(cv2.CAP_PROP_FPS)
frames_per_second = int(frame_rate)

success, frame = video.read()
frame_counter = 0
second_counter = 0
 
while success:
      if frame_counter % frames_per_second == 0:
         resized_frame = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
         image_path = os.path.join(destination_folder, f'B{second_counter}.jpg')
         cv2.imwrite(image_path, resized_frame)
         second_counter += 1
      success,frame = video.read()
      frame_counter += 1
video.release()

