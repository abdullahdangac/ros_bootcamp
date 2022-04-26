#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def counter():
    rospy.init_node('counter', anonymous=True)
    pub = rospy.Publisher('count', Int32, queue_size=10)

    rospy.loginfo("Counter Started")
    cnt = 0
    while not rospy.is_shutdown():
        cnt += 1
        pub.publish(cnt)
        rospy.loginfo(cnt)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        counter()
    except rospy.ROSInterruptException:
        pass
