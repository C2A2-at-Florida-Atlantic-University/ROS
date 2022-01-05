#include <ros/ros.h>
#include <geometry_msgs/Point.h>

geometry_msgs::Point pos;
void markerCallback(const geometry_msgs::Point::ConstPtr& msg)
{
  pos = *msg;
  ROS_INFO("\nPosition:\n\tx:%f\n\ty:%f\n\tz:%f", pos.x, pos.y, pos.z);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "marker_node_sub");
  ros::NodeHandle n;
  ros::Subscriber sub1 = n.subscribe("/marker_pos", 500, markerCallback);
  ros::spin();
  

  return 0;
}