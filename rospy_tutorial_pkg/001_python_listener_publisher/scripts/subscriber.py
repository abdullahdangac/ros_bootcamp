#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Int32

callback_flag = 0

def callback(data):
    global callback_flag
    rospy.loginfo(data.data)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.data)

    callback_flag = 1
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("count", Int32, callback)

    if callback_flag == 0:
        rospy.loginfo("Waiting for counter to start...")

    rospy.spin()

if __name__ == '__main__':
    listener()

