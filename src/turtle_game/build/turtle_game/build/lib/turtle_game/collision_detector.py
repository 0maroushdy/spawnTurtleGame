#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import math

class CollisionDetectorNode(Node):
    def __init__(self):
        super().__init__("collision_detector_node")
        self.create_subscription(Pose, 'base_turtle/pose', self.base_pose_callback, 10)
        self.target_pose_subscriptions = []
        self.base_pose = None

    def base_pose_callback(self, msg):
        self.base_pose = msg
        self.check_for_collisions()

    def check_for_collisions(self):
        if self.base_pose:
            for target_pose in self.target_pose_subscriptions:
                distance = math.sqrt(
                    (self.base_pose.position.x - target_pose.position.x) ** 2 +
                    (self.base_pose.position.y - target_pose.position.y) ** 2
                )
                if distance < 0.7:
                    self.get_logger().info("Target caught!")

def main(args=None):
    rclpy.init(args=args)
    node = CollisionDetectorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
