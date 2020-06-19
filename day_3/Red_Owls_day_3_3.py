# -*- coding: utf-8 -*-
import numpy as np
import math
import cv2
import time
import roslib
import sys
import rospy
from pyzbar import pyzbar
from sensor_msgs.msg import Image
import threading
from cv_bridge import CvBridge, CvBridgeError

from clever import srv
from std_srvs.srv import Trigger

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

class ColorDetecting():                                                                                              # Класс для распознавание цветов - желтый, синий, красный
    def __init__(self):                                                                                              # Функция init содежит:
        rospy.init_node('Color_detect', anonymous=True)                                                              # Создание ноды
        self.bridge = CvBridge()                                                                                     # Переменная необходимая для конвертации изображения из типа msg в обычный вид и обратно
        self.image_sub = rospy.Subscriber("main_camera/image_raw",Image,self.callback)                               # Подписание на топик с изображением
    def callback(self,data):                                                                                         # Основная функция (data- изображения из типа msg)
        try:                                                                                                         # Считывание и конвертация изображения в вид пригодный для дальнейшей работы (try- для отсутствия ошибки если топик будет пустой)
          img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except:pass
        Grey = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def main():                                                                                                      # Начальная функция
  global col_det
  col_det = ColorDetecting()                                                                                         # Обращение к классу Color_detect

main()

print navigate(x=0, y=0, z=1, speed=0.5, frame_id='body', auto_arm=True)
rospy.sleep(3)

print navigate(x=0.5, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
col_det.Qr = True
print('Захар делай скрин')
print('Qr detect:' + col_det.land)
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=0.5, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=0.5, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=0.5, y=1.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=0.5, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=0.5, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=1.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=1.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=1.5, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=1.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=0.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=0.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=1.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=1.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=2.3, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print navigate(x=2.5, y=2.8, z=1.2, speed=0.5, yaw=math.radians(90), frame_id='aruco_map')
print('Захар делай скрин')
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True
rospy.sleep(3)
start = get_telemetry(frame_id='aruco_map')
print(start.x,start.y,start.z)
col_det.Color = True

print('Qr detect:' + col_det.land)
if col_det.land in col_det.lan:
    x1 = col_det.lan[col_det.Qr][0]
    y1 = col_det.lan[col_det.Qr][1]
    print navigate(x=x1, y=y1, z=1, speed=0.5, yaw=math.radians(90),frame_id='aruco_map')
else:
    print navigate(x=1, y=1, z=1, speed=0.5, yaw=math.radians(90),frame_id='aruco_map')
rospy.sleep(10)

land()
