from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
        output='screen',
    )

    diffbot_base_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diffbot_base_controller'],
        output='screen',
    )

    return LaunchDescription([joint_state_broadcaster_spawner, diffbot_base_controller_spawner])