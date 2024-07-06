# irp_ros
Docker should be installed before proceeding with the next steps You can follow this link for docker setup on Ubuntu

Clone this package git clone https://github.com/mzahana/px4_ros2_humble
Build the docker image
cd px4_ros2_humble/docker
make px4-dev-simulation-ubuntu22
This builds a Docker image that has the required PX4 development environment, and ROS 2 Humble Desktop. It does not container the PX4 source code or any ROS 2 workspaces. This is covered in the following sections.

The Gazebo version in the provided Docker image is Gazebo Garden.

Run
If you have NVIDIA GPU, run

./docker_run_nvidia.sh
Otherwise, run

./docker_run.sh
NOTE

Source files and workspaces should be saved inside a shared volume. The path to the shared volume inside the container is /home/user/shared_volume. The path to the shared volume in the host is $HOME/px4_ros2_humble_shared_volume.
When you login inside the container, the username is user and the passwrod is user. user is part of the sudo group and can install pckages using sudo apt install
Install PX4
It's recommended to have the PX4-Autopilot src and the ros 2 workspace(s) inside the shared volume, so you don't lose them if the container is removed.

Enter the container ./docker_run_nvidia.sh or ./docker_run.sh
Go to the shared volume cd /home/user/shared_volume
Clone the PX4-Autopilot source
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
cd PX4-Autopilot/
make px4_sitl

Note that the above commands will install the recommended simulator for your version of Ubuntu. If you want to install PX4 but keep your existing simulator installation, run ubuntu.sh above with the --no-sim-tools flag.

For more information and troubleshooting see: Ubuntu Development Environment and Download PX4 source.

Some Python dependencies must also be installed (using pip or apt): pip install --user -U empy==3.3.4 pyros-genmsg setuptools

Setup Micro XRCE-DDS Agent & Client
For ROS 2 to communicate with PX4, uXRCE-DDS client must be running on PX4, connected to a micro XRCE-DDS agent running on the companion computer.

Setup the Agent
The agent can be installed onto the companion computer in a number of ways. Below we show how to build the agent "standalone" from source and connect to a client running on the PX4 simulator.

To setup and start the agent:

Open a terminal : 
To do so : 
- ctrl + alt + T 
- check the ID of the current container : docker ps
- docker exec -it <ID> bash
- Navigate to the current directory cd /home/user/shared_volume
  
Enter the following commands to fetch and build the agent from source:

git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git
cd Micro-XRCE-DDS-Agent
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig /usr/local/lib/

MicroXRCEAgent udp4 -p 8888

New terminal :  docker exec -it <ID> bash
cd /home/user/shared_volume
mkdir ros2_ws/src
cd ros2_ws/src
Clone the px4_msgs repo to the /src directory (this repo is needed in every ROS 2 PX4 workspace!): git clone https://github.com/PX4/px4_msgs.git
Clone the example repository px4_ros_com to the /src directory: git clone https://github.com/PX4/px4_ros_com.git
Source the ROS 2 development environment into the current terminal and compile the workspace using colcon:
cd ..
source /opt/ros/humble/setup.bash
colcon build
Source the local_setup.bash: source install/local_setup.bash

Launch the example.
ros2 run px4_ros_com offboard_control
The vehicle should arm, ascend 5 metres, and then wait (perpetually).







