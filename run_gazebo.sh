#!/bin/bash

sudo killall gzserver
sudo killall gzclient
sudo killall rviz
sudo killall roscore
sudo killall rosmaster

#roslaunch sambot_gazebo sambot_world.launch
roslaunch [package_name] [launch_file_name]

