import rclpy
from rclpy.node import Node
from lifecycle_msgs.msg import TransitionEvent

class GoalStatusSubscriber(Node):
    def __init__(self):
        super().__init__('goal_status_subscriber')
        self.subscription = self.create_subscription(
            TransitionEvent,
            '/bt_navigator/transition_event',
            self.goal_status_callback,
            10
        )
        
    def goal_status_callback(self, msg):
        if msg.label == "Goal succeeded":
            self.get_logger().info("Wrongly parked vehicles; Reporting to the owner")

def main(args=None):
    rclpy.init(args=args)
    goal_status_subscriber = GoalStatusSubscriber()
    rclpy.spin(goal_status_subscriber)
    goal_status_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
