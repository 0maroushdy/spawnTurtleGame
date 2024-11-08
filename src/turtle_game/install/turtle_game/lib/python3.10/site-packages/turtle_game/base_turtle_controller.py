#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ControllerNode(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.publisher_ = self.create_publisher(Twist, 'base_turtle/cmd_vel', 10)
        self.timer_ = self.create_timer(0.05, self.publish_velocity)

    def publish_velocity(self):
        twist = Twist()
        twist.linear.x = 1.0
        twist.angular.z = 0.5
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
