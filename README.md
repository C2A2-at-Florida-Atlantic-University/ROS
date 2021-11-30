# ROS
Installation Of Ubuntu:
While there are many versions of ROS, we will be using ROS Melodic to make things easier to manage since it is the most stable

In order to even download ROS, you need to install Ubuntu 18.04 here at https://releases.ubuntu.com/18.04/ubuntu-18.04.6-desktop-amd64.iso 

Once you download, in order for you to put the image on a USB or SD/Micro-SD you need to flash the image using https://www.balena.io/etcher/ and download it for whatever system you are using.

Once you download etcher, upload the Ubuntu image and then select your USB or SD/Micro-SD to flash it onto and it should flash Ubuntu 18.04 on whatever you are using.

Reboot your computer and go on to boot options on your BIOS to select whatever you flashed Ubuntu 18.04 onto as your booting device.

Follow the instructions on the installation and decide whether you want to dual-boot or wash your original operating system.

Once finished, launch Ubuntu 18.04 after unplugging the installation USB or SD/Micro-SD and we will proceed to the installation of ROS

Installation Of ROS Melodic:

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

Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS. If you have not yet installed rosdep, do so as follows.

```
sudo apt install python-rosdep
```

With the following, you can initialize and update rosdep.

```
sudo rosdep init
rosdep update
```


