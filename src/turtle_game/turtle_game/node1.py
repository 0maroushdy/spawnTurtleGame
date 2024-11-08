#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 

#This is a testing file and a testing node, msh el tast el matlob
class MyNode(Node):
    def __init__(self):
        super().__init__("Node1")
        self.get_logger().info("Hey, Node was created successfully ^_^ ")
        self.counter_1 = 0
        self.create_timer(1.0, self.timer_printer)

    def timer_printer(self):
        self.get_logger().info("Node is running " + str(self.counter_1))
        self.counter_1 += 1



# The main function
def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    # Shutting down ROS communi.
    rclpy.shutdown()

if __name__ == '__main__':
    main()
