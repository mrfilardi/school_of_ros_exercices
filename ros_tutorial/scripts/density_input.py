#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node("density_input")
density_pub = rospy.Publisher("/density", Float64 , queue_size=10)

density = float(input("Input density: "))

while not rospy.is_shutdown():
	density_pub.publish(density)
	rospy.sleep(0.1)
	
