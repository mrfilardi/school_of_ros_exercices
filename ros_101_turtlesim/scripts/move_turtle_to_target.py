#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import math

#variables
position_x = rospy.get_param("/goal_x")
position_y = rospy.get_param("/goal_y")
threshold_goal = rospy.get_param("/threshold")
current_x = 0
current_y = 0

rospy.init_node('move_turtle_to_target')

def pose_callback(data):
	global current_x
	global current_y
	current_x = data.x
	current_y = data.y

publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

msg = Twist()

while not rospy.is_shutdown():
    
    if ((position_x-threshold_goal) < current_x and (position_x+threshold_goal) > current_x and
        (position_y-threshold_goal) < current_y and (position_y+threshold_goal) > current_y) :
        rospy.loginfo("Target Reached!!!")
    else: 
        rospy.logdebug("Current Pos -> X: %s, Y: %s", current_x, current_y)    
        rospy.loginfo("Current Pos -> X: %s, Y: %s", current_x, current_y)    
        rospy.loginfo("Moving to Point X: %s, Y: %s ->Threshold %s", position_x, position_y, threshold_goal)
        
    time.sleep(0.1)
    