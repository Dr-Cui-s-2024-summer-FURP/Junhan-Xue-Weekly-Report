import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
import numpy as np

class PointCloudSaver(Node):
    def __init__(self):
        super().__init__('point_cloud_saver')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/livox/lidar',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Convert PointCloud2 message to numpy array
        pc_data = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
        points = np.array(list(pc_data))

        # Save to txt file
        np.savetxt('point_cloud_data.txt', points, fmt='%.6f', header='x y z')
        self.get_logger().info('Point cloud data saved to point_cloud_data.txt')

        # Shutdown node after saving data
        self.get_logger().info('Shutting down node...')
        self.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    point_cloud_saver = PointCloudSaver()
    rclpy.spin(point_cloud_saver)

if __name__ == '__main__':
    main()

