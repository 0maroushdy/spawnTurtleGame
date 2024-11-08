#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class BaseTurtleController(Node):
    def __init__(self):
        super().__init__('base_turtle_controller')
        self.publisher = self.create_publisher(Twist, 'turtle-velocity', 10)

        # Timer to update The turtel movement
        self.timer = self.create_timer(0.05, self.move_turtle)

    def move_turtle(self):
        twist = Twist()
        twist.linear.x = 1.0  
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = BaseTurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
