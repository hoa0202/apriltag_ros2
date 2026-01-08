from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        # Arguments
        DeclareLaunchArgument(
            'image_topic',
            default_value='/zed/zed_node/rgb/image_rect_color',
            description='Input image topic'
        ),
        DeclareLaunchArgument(
            'camera_info_topic',
            default_value='/zed/zed_node/rgb/camera_info',
            description='Camera info topic'
        ),
        DeclareLaunchArgument(
            'params_file',
            default_value=PathJoinSubstitution([
                FindPackageShare('apriltag_ros'), 'cfg', 'tags_25h9.yaml'
            ]),
            description='Path to params file'
        ),

        # Node
        Node(
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag_node',
            remappings=[
                ('image_rect', LaunchConfiguration('image_topic')),
                ('camera_info', LaunchConfiguration('camera_info_topic')),
            ],
            parameters=[LaunchConfiguration('params_file')],
            output='screen',
        ),
    ])
