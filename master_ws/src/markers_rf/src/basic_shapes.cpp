#include <ros/ros.h>
#include <visualization_msgs/Marker.h>
#include <std_msgs/String.h>

geometry_msgs::Point pos;
void markerCallback(const geometry_msgs::Point::ConstPtr& msg)
{
  pos = *msg;
  ROS_INFO("\nPosition:\n\tx:%f\n\ty:%f\n\tz:%f", pos.x, pos.y, pos.z);
}

int main( int argc, char** argv )
{
  ros::init(argc, argv, "marker_goal");
  ros::NodeHandle n;
  ros::Subscriber sub1 = n.subscribe("/hps_pos", 500, markerCallback);
  ros::spinOnce();


  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 500);
  ros::Rate r(1);
  ros::spinOnce();

  int count = 0;
  while (ros::ok())
  {
    visualization_msgs::Marker marker;
    marker.header.frame_id = "/map"; //Frame
    marker.header.stamp = ros::Time::now();
    marker.ns = "marker_goal"; // Namespace
    marker.id = 0;
    marker.type = visualization_msgs::Marker::SPHERE;
    marker.action = visualization_msgs::Marker::ADD;
    marker.pose.position.x = pos.x;
    marker.pose.position.y = pos.y;
    marker.pose.position.z = 1;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;
    marker.scale.x = 0.5;
    marker.scale.y = 0.5;
    marker.scale.z = 0.5;
    marker.color.r = 0.0f;
    marker.color.g = 1.0f;
    marker.color.b = 0.0f;
    marker.color.a = 1.0;
    marker.lifetime = ros::Duration();
    while (marker_pub.getNumSubscribers() < 1)
    {
      if (!ros::ok())
      {
        return 0;
      }
      ROS_WARN_ONCE("Please create a subscriber to the marker");
      ros::Duration(1.0).sleep();
    }
    marker_pub.publish(marker);
    ros::spinOnce();
    r.sleep();
    ++count;
  }
}