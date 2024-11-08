from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Controller Node
        Node(
            package='turtle_game',
            executable='base_turtle_controller',  
            name='controller_node',        
            output='screen'
        ),
        # Spawner Node
        Node(
            package='turtle_game',
            executable='turtle_spawner',    
            #name='spawner_node',           
            output='screen'
        ),
        # Collision Detector Node
        Node(
            package='turtle_game',
            executable='collision_detector',  
            #name='collision_detector_node',        
            output='screen'
        ),
    ])
