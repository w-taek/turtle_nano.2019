#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray
import numpy as np
import Jetson.GPIO as gpio

DEBUG = True

global channels
channels = [11, 13, 15, 36, 38, 40]
gpio.setmode(gpio.BOARD)

def callback(count):
    count_arr = count.data
    
    if (DEBUG):
        print("----------------------------")
        print("left : ", count_arr[:3])
        print("right: ", count_arr[3:])
        print("----------------------------")
    
    for i in range(6):
        if count_arr[i] == 1:
            gpio.output(channels[i], gpio.HIGH)
        elif count_arr[i] == 0:
            gpio.output(channels[i], gpio.LOW)

def sub_count():
    gpio.setup(channels, gpio.OUT)
    rospy.init_node('result_count_sub', anonymous = True)
    rospy.Subscriber('detect_count', Int32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    sub_count()
    gpio.cleanup(channels)
