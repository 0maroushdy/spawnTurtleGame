#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 

class MyNode(Node):
    def __init__(self):
        super().__init__("Node1")
        self.get_logger().info("Hey, Node was created sucssefully ^_^ ")


#the main ------------------
def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    
    # shuting down ros communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()