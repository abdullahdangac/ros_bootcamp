#!/usr/bin/env python

import rospy
from rospy_tutorial_pkg.msg import NewPose

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', NewPose, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pose = NewPose()
        pose.x = 47.95
        pose.y = 83.57
        pose.heading = 3.14

	text = "x: {}      ".format(pose.x) + \
               "y: {}      ".format(pose.y) + \
               "heading: {}".format(pose.heading)

        rospy.loginfo(text)
        pub.publish(pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
