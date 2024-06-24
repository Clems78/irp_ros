ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}
ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip

#Install rviz2
RUN apt install ros-${ROS_DISTRO}-rviz2 -y

# Gazebo Fortress
# Set the working directory
WORKDIR /root

# Install the necessary packages
RUN apt-get update && apt-get install -y \ 
    lsb-release \ 
    wget \ 
    gnupg \
    x11-apps \
    libxext-dev \
    libxrender-dev \
    libxtst-dev 

RUN sudo apt-get install  -y ros-${ROS_DISTRO}-ros-gz

RUN apt install -y vim
RUN apt install -y htop
RUN apt install -y nvtop 

# Set the default shell to bash
ENV SHELL /bin/bash

# Source the ROS setup script
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> /etc/bash.bashrc
RUN echo "source /ros2_humble_ws/install/setup.bash" >> ~/.bashrc

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME
CMD ["/bin/bash"]