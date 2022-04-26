#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float64


class Random():
    def __init__(self):
        rospy.init_node('Random', anonymous=True)
        self.pub = rospy.Publisher('random', Float64, queue_size=10)
        self.rate = rospy.Rate(1)

    def get_random(self):
        msg = Float64()
        while not rospy.is_shutdown():
            msg.data = random.uniform(0,100)
            rospy.loginfo(msg)

            self.pub.publish(msg)
            self.rate.sleep()

def main():
    rnd = Random()
    rnd.get_random()


if __name__ == '__main__':
    main()
