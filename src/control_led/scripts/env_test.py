#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray
import numpy as np
import Jetson.GPIO as gpio


DEBUG = True
count_arr = []
# global channels
# channels = [36, 38, 40]
# gpio.setmode(gpio.BOARD)
# gpio.setup(channels, gpio.OUT)

import rospy                    
from std_msgs.msg import UInt8

def callback(count):
    global count_arr
    for i in range(len(count.data)):
        count_arr.append(count.data[i])
    s = "count array[0] %u\n" % count_arr[0]
    # count_arr = count.data
    
    # if (DEBUG):
    #     for i in ranges(3):
    #         print("channels :", channels[i], "    |    ", "count :",  count_arr[i])
    
    # for i in ranges(3):
    #     gpio.output(channels[i], count_arr[i])


def sub_count():
    rospy.init_node('result_count_sub', anonymous = True)
    rospy.Subscriber('/detect_count', UInt8, callback)
    # gpio.cleanup(channels)
    

if __name__ == '__main__':
    sub_count()
    rospy.spin()