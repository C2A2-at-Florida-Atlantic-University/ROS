# ROS Tutorial
### Installation Of Ubuntu:
While there are many versions of ROS, we will be using ROS Melodic to make things easier to manage since it is the most stable

In order to even download ROS, you need to install Ubuntu 18.04 here at https://releases.ubuntu.com/18.04/ubuntu-18.04.6-desktop-amd64.iso 

Once you download, in order for you to put the image on a USB or SD/Micro-SD you need to flash the image using https://www.balena.io/etcher/ and download it for whatever system you are using.

Once you download etcher, upload the Ubuntu image and then select your USB or SD/Micro-SD to flash it onto and it should flash Ubuntu 18.04 on whatever you are using.

Reboot your computer and go on to boot options on your BIOS to select whatever you flashed Ubuntu 18.04 onto as your booting device.

Follow the instructions on the installation and decide whether you want to dual-boot or wash your original operating system.

Once finished, launch Ubuntu 18.04 after unplugging the installation USB or SD/Micro-SD and we will proceed to the installation of ROS

### Installation of ROS Melodic:

On your terminal, first install python3 and pip3 with these commands to avoid errors with certain ROS libraries

```
sudo apt update
sudo apt install python3
sudo apt-get -y install python3-pip
```

Now we can install ROS Melodic

On a new terminal type down these commands,

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Then type this if haven't installed it already
```
sudo apt install curl
```
Combine the two commands below

```
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

Then in order to implement the installation:

```
sudo apt update
sudo apt install ros-melodic-desktop-full
```

Once installed, use these commands to configure your enviroment

```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
If you just want to change the environment of your current shell, instead of the above you can type:

```
source /opt/ros/melodic/setup.bash
```

To install the tool and other dependencies in order to build ROS packages, run:

```
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS. With the following, you can initialize and update rosdep.

```
sudo rosdep init
rosdep update
```

### Catkin/CMake Installation and ROS Workspace Creation:

To install catkin paste this into the terminal:
```
sudo apt-get install ros-melodic-catkin
```
Now to access the installation:
```
source /opt/ros/melodic/setup.bash
```
Then to build your ROS Workspace in your home directory:
```
mkdir -p ~/navigation_ws/src
cd ~/navigation_ws/
catkin_make
```

Now to add your Workspace as your default workspace:
```
source devel/setup.bash
echo $ROS_PACKAGE_PATH
```

### Turtlebot Configuration:

In order to install dependent ROS Packages needed before doing turtlebot on ROS, copy and paste those links on to the terminal:

```
sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy \
  ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc \
  ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \
  ros-melodic-rosserial-arduino ros-melodic-rosserial-python \
  ros-melodic-rosserial-server ros-melodic-rosserial-client \
  ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \
  ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro \
  ros-melodic-compressed-image-transport ros-melodic-rqt* \
  ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers
```
Now You Install TurtleBot3 via Debian Packages here:
```
sudo apt-get install ros-melodic-dynamixel-sdk
sudo apt-get install ros-melodic-turtlebot3-msgs
sudo apt-get install ros-melodic-turtlebot3
```
Set the default TURTLEBOT3_MODEL name to your model. Enter the below command to a terminal.

In case of TurtleBot3 Burger:
```
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```
In case of TurtleBot3 Waffle Pi:
```
$ echo "export TURTLEBOT3_MODEL=waffle_pi" >> ~/.bashrc
```
### Basic Turtlebot Navigation:

Install the Navigation Package for Gazebo:

```
cd ~/navigation/src/
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/navigation_ws && catkin_make
```

Launch Empty World on Gazebo:

```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
Launch TurtleBot3 World on Gazebo:

```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
Launch TurtleBot3 House on Gazebo:

```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
How to Teleoperate the Turtlebot on Gazebo:

In order to teleoperate the TurtleBot3 with the keyboard, launch the teleoperation node with below command in a new terminal window or tab:

```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

