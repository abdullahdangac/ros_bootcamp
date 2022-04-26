#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64


class Listener:
    def __init__(self):
        rospy.init_node('Listener', anonymous=True)
        self.sub = rospy.Subscriber("random", Float64, self.callback)
        self.random = 0

    def callback(self, data): 
        self.random = data.data

    def print_random(self):
        rospy.loginfo(self.random)


def main(args):  
    listener = Listener()
 
    while not rospy.is_shutdown():
        listener.print_random()
        rospy.sleep(1)


if __name__ == '__main__':
    main(sys.argv)
