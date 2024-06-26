from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    pkg_irp_pkg = FindPackageShare(package='irp_pkg').find('irp_pkg')
    world_path = os.path.join(pkg_irp_pkg, 'worlds', 'empty_with_duck.world')
    
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_irp_pkg, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'world': world_path}.items(),
        ),
        Node(
            package='irp_pkg',
            executable='my_node',
            name='my_node',
            output='screen',
        ),
    ])
