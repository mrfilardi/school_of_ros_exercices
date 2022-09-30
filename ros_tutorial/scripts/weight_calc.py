#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Weight

from math import pi

density =0
height =0
radius_squared=0

density_found = False
radius_squared_found = False
height_found = False

def density_callback(data):
    global density
    global density_found 
    density = data.data
    density_found = True

def radius_squared_callback(data):
    global radius_squared
    global radius_squared_found 
    radius_squared = data.data
    radius_squared_found = True

def height_callback(data):
    global height
    global height_found
    height = data.data
    height_found = True

def calculate():
    if density_found and radius_squared_found and height_found:
        msg = Weight()
        msg.weight = pi * radius_squared * height * density
        pub.publish(msg)

rospy.init_node("weight_calc")
rospy.Subscriber("/height", Float64, height_callback)
rospy.Subscriber("/radius_squared",Float64 , radius_squared_callback)
rospy.Subscriber("/density",Float64 , density_callback)
pub = rospy.Publisher("/weight", Weight, queue_size=10)

while not rospy.is_shutdown():
    calculate()
    rospy.sleep(0.1) 
