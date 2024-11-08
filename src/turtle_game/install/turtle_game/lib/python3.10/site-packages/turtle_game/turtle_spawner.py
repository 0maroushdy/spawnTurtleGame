#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import random

class SpawnerNode(Node):
    def __init__(self):
        super().__init__("spawner_node")
        self.spawn_turtle()

    def spawn_turtle(self):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        # Publish the position of the new target turtle

def main(args=None):
    rclpy.init(args=args)
    node = SpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
