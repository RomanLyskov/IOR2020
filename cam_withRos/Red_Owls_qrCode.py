# -*- coding: utf-8 -*-
import time
import math
import numpy as np
import rospy
import cv2
from pyzbar import pyzbar
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

rospy.init_node('fff') # Создание ноды
image_pub = rospy.Publisher("QR", Image,queue_size=10) # Создание топика для вывода финального изображения
bridge = CvBridge()


def image_callback(data):   # Функция для нахождения и распознования QR кодов
    frame = bridge.imgmsg_to_cv2(data, 'bgr8')      # Считывание изображения
    barcodes  = pyzbar.decode(frame)    # Распознование QR-кодов
    if barcodes:    # Если они на картинке есть
        texts = []
        for bar in barcodes:       # Проходит по всем QR кодам, которые он нашел

            (x, y, w, h) = bar.rect     # Координаты QR кода

            barcodeData = bar.data.decode("utf-8") # Записывает в переменную информацию, находящуюся в данном коде

            texts.append([barcodeData, (x,y,w,h)])  # Сохраняет в список данные из QR кода и его координаты

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)    # Выделение по контуру на изоображении
            cv2.putText(frame, str(barcodeData), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.2, (0, 0, 255), ) # Выводит данные QR кода над ним 
    image_pub.publish(bridge.cv2_to_imgmsg(frame, 'bgr8'))

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback, queue_size=1) # Подписание на топик с изображением

rospy.spin() # Обязательная функция для работы с топиками
