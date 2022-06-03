# Multirobot Turtlebot3 Simulation Exploration based on RRT for Ubuntu 18.04 ROS Melodic
This package is a compilation of the RRT package in a much complete package rather than figuring map merging and other function from other resipotary. 
This would serve as a self-contained package for the exploration module using simulation for the turtlebot.
This is tested on Ubuntu 18.04LTS with ROS Melodic.

credit to hasauino for creating the RRT exploration packages.

[RRT Exploration package](https://github.com/hasauino/rrt_exploration "RRT Exploration").

[RRT Exploration Tutorial package](https://github.com/hasauino/rrt_exploration_tutorials "RRT Exploration").


## Requirements
The following code is exectuted in ROS Melodic in Ubuntu 18.04 LTS

The following libraries are required to install before proceeding to run the code

    $ sudo apt-get install ros-melodic-gmapping
    $ sudo apt-get install ros-melodic-navigation
    $ sudo apt-get install python-opencv
    $ sudo apt-get install python-numpy
    $ sudo apt-get install python-scikits-learn
    $ sudo apt-get install ros-melodic-teb-local-planner


## Installation Process
create a new folder called "catkin_explore/src" by executing the following comment:

    $ sudo mkdir -p ~/catkin_explore/src
    $ cd ~/catkin_explore/src/
    $ git clone https://github.com/hikashi/multi-robot-rrt-exploration-melodic.git
    $ cd ~/catkin_explore
    $ catkin_make

## Add in Amazon Map
add in the amazon world map by executing the following comments:

    $ cd ~/catkin_explore/src
    $ git clone https://github.com/aws-robotics/aws-robomaker-small-house-world.git
    $ git clone https://github.com/aws-robotics/aws-robomaker-bookstore-world.git
    $ cd ~/catkin_explore/
    $ catkin_make
    

## Execution for Single Robot
The program can be executed using the following comments in three terminal:

Terminal 1

     # roscore 
Terminal 2

     # source ~/catkin_explore/devel/setup.bash 
     # export TURTLEBOT3_MODEL=waffle_pi
     # roslaunch ros_multitb3 single_tb3_house.launch
Terminal 3

     # source ~/catkin_explore/devel/setup.bash 
     # export TURTLEBOT3_MODEL=waffle_pi
     # roslaunch rrt_exploration single_tb3_exploration.launch 

## Execution for Multirobot
The program can be executed using the following comments in three terminal:

Terminal 1

     # roscore 
Terminal 2

     # source ~/catkin_explore/devel/setup.bash 
     # export TURTLEBOT3_MODEL=waffle_pi
     # roslaunch ros_multitb3 multi_tb3_house.launch 
Terminal 3

     # source ~/catkin_explore/devel/setup.bash 
     # export TURTLEBOT3_MODEL=waffle_pi
     # roslaunch rrt_exploration multi_tb3_exploration.launch 



## Exploration Process
The exploration relies on the correct sequence else rendering with no goal for each of the robot.
1. Top Left
2. Bottom Left
3. Bottom Right
4. Top Right
5. Initial Point
 ![Instruction](/instruction2.png)
 Things to note: 5th initial point should be within the known map or preferable close to the robot starting point. 
 
 
## Saving Map
Save the map using the following command:

    # rosrun map_server map_saver -f mymap
    
## How to speed up Gazebo
- Try to download the [online models](https://github.com/osrf/gazebo_models) and put inside "~/.gazebo/models/" folder 
- Try not run a lot process in the background (simulation is cpu intensive)
- RVIZ might take up some of the computing power, can try to drop some topic if needed.

## known issues
1. the map merging will shift a lot if the slam drifting too severe.
2. shifting causing the frontier point remains even after explored.
3. sometimes robots will take some time to move to new plan.
4. The revenue function is awkwardly computing large negative value and hence the navigation cost seem insignificant. (inherited from the original RRT exploration)
5.  assignment of the goal is not close to suboptimal. May need to perform optimization on the goal allocation.
