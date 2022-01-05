#!/usr/bin/env python2
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

x = 0.0
y = 0.0 
theta = 0.0
x_0 = 0.0
y_0 = 0.0
tt = 0.0
tt2 = 0.0

def newOdom(msg):
    global x
    global y
    global theta
    global tt

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    tt = x + y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def otherRobot(msg2):
    global x_0
    global y_0
    global tt2

    x_0 = msg2.pose.pose.position.x
    y_0 = msg2.pose.pose.position.y
    tt2 = x_0 + y_0

rospy.init_node("rf_burger", anonymous=True)

sub = rospy.Subscriber("/burger/odom", Odometry, newOdom)
sub2 = rospy.Subscriber("/waffle_pi/odom", Odometry, otherRobot)
pub = rospy.Publisher("/burger/cmd_vel", Twist, queue_size = 1)

speed = Twist()

r = rospy.Rate(5)

goal = Point()

def callback(data):
    goal.x = data.x
    goal.y = data.y
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', (goal.x, goal.y))

    return goal.x, goal.y


while not rospy.is_shutdown():
    rospy.Subscriber('hps_pos',Point, callback)
    inc_x = goal.x - x
    inc_y = goal.y - y

    angle_to_goal = atan2(inc_y, inc_x)

    if tt >= tt2:
        if abs(angle_to_goal - theta) > 0.1:
            speed.linear.x = 0.0
            speed.angular.z = 0.3
        else:
            speed.linear.x = 0.2
            speed.angular.z = 0.0

    pub.publish(speed)
    r.sleep()