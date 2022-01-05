#!/usr/bin/env python2

import rospy
import numpy as np
import pylab as pl
from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from std_msgs.msg import Float64
from nav_msgs.msg import OccupancyGrid

# VARIABLE DECLARATION
i = 0
gamma = 0.75
current_state = 0
initial_state = 1
Rewards = []
path = [current_state]

# MATRIX SETUP  
MATRIX_SIZE = 11
Matrix = np.matrix(np.ones(shape = (MATRIX_SIZE, MATRIX_SIZE)))
Matrix *= -1

# Q MATRIX DECLARATION
Q = np.matrix(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))


Nodes = [(0,1), (1,5), (5,6), (1,4), (1,2), (1,3), (9,10), (8,10), (2,4), (0,6), (6,7), (8,9), (7,8), (1,7), (4,9)]

#def map_callback(data):
	#rospy.loginfo(rospy.get_caller_id() + ' The map is being processed!')
	#map_data = np.empty((385,385), float)
	#map = np.append(map_data, data)

	#if(map[map  == -1]):
		#index = np.where(map == -1)
		#print index

		#loc = index + 1
		#np.delete(map, loc[0], loc[1])

	#print(map)

#sub = rospy.Subscriber('map',OccupancyGrid, map_callback)  

def rf_callback(data):
	#rospy.loginfo(rospy.get_caller_id() + 'I heard %s',(data.x, data.y, data.z))

	pub = rospy.Publisher('hps_pos', Point, queue_size = 10)
	rate = rospy.Rate(10)
	pub.publish(data)


# COLLABORATION FUNCTION TO ALLOW BOTH ROBOTS TO AGREE ON THE HIGHEST RF SIGNAL POINT
def Collaboration():
        rospy.init_node('imu_listener', anonymous = True)
	rospy.Subscriber('/burger/imu',Point, rf_callback)
	rospy.Subscriber('/waffle/imu',Point,rf_callback)
	rospy.spin()
   
   	Robot1 = rf_callback
  	Robot2 = rf_callback

   	if  Robot1 == Robot2:
     		decision = Robot1 
     		goal = decision
     		return goal

	elif Robot1 > Robot2:
		decision = Robot1
		goal = decision
		return goal

	elif Robot2 > Robot1:
		decision = Robot2
		goal = decision
		return goal

       

Collaboration()

def Double_Size(n):
  new_n = n * 2
  n = new_n

def Triple_Size(n):
  new_n = n * 3
  n = new_n

def Matrix_Editing(n, data):
  for x in data:
    if data.resize(n,n) == data.resize(8,8):
      Double_Size(n)
    else:
      Triple_Size(n)


# GOAL CHOICE FUNCTION 
def Goal_Choice(Nodes):

    goal = Collaboration()

    n = 8;
    data = [23, 45, 67, 0, 12, 34, 56, 48,  89, 43, 13, 4, 7, 55, 50, 30,   1, 5, 17, 3, 32, 28, 84, 75,   44, 33, 20, 25, 70, 67, 66, 40, 83, 9, 51, 64, 78, 10, 22, 66,  27, 59, 88, 77, 6, 18, 39, 28,  24, 57, 47, 6, 10, 17, 89, 90,  38, 79, 60, 63, 14, 11, 52, 59]

    RF_Matrix = np.matrix(data).reshape((n,n))
    print "\n","Matrix of Points:\n"
    print RF_Matrix
    print "\n"

    return goal,n,data

#Matrix_Editing(n,data)

Goal_Choice(Nodes)

# POINT ALLOCATION FOR GOAL SPOTS AND NON-GOAL SPOTS
goal = 10

for point in Nodes:
    if point[1] == goal:
        Matrix[point] = 100
    else:
        Matrix[point] = 0
  
    if point[0] == goal:
        Matrix[point[::-1]] = 100
    else:
        Matrix[point[::-1]]= 0
  
Matrix[goal, goal]= 100


# AVAILABLE ACTIONS FUNCTION TO ALLOW FOR GENERATION OF A RANDOM ACTION
def available_actions(state):
    current_state_row = Matrix[state, ]
    available_action = np.where(current_state_row >= 0)[1]
    return available_action
  
available_action = available_actions(initial_state)
  
# SAMPLE NEXT ACTION FUNCTION TO TEST THE NEXT ACTION
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_action, 1))
    return next_action

action = sample_next_action(available_action)

# UPDATE FUNCTION TO UPDATE THE Q MATRIX BASED ON THE ACTION TAKEN
def update(current_state, action, gamma):
    max_index = np.where(Q[action, ] == np.max(Q[action, ]))[1]
    if max_index.shape[0] > 1:
         max_index = int(np.random.choice(max_index, size = 1))
    else:
         max_index = int(max_index)

    max_value = Q[action, max_index]
    Q[current_state, action] = Matrix[current_state, action] + gamma * max_value

    if (np.max(Q) > 0):
        return (np.sum(Q / np.max(Q)*100))
    else:
        return (0)

update(initial_state, action, gamma)

# RUNS FOR 500 ITERATIONS 
for i in range(500):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_action = available_actions(current_state)
    action = sample_next_action(available_action)
    Reward = update(current_state, action, gamma)
    Rewards.append(Reward)

while current_state != 10:
    next_location_index = np.where(Q[current_state, ] == np.max(Q[current_state, ]))[1]

    if next_location_index.shape[0] > 1:
          next_location_index = int(np.random.choice(next_location_index, size = 1))

    else:
        next_location_index = int(next_location_index)
    path.append(next_location_index)
    current_state = next_location_index

#print "Path taken by the AI:", path, "\n"

print "\n", "Trained Q-Matrix:", "\n"

print Q/ np.max(Q) * 100

pl.plot(Rewards)
pl.title('Revards vs. Iterations')
pl.xlabel('Number of Iterations')
pl.ylabel('Rewards Gained')
pl.show()
