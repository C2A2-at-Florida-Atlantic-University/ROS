#include <ros/ros.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Odometry.h>

#include <sstream>

nav_msgs::Odometry pos1;
nav_msgs::Odometry pos2;
void pos1Callback(const nav_msgs::Odometry::ConstPtr& msg)
{
  pos1 = *msg;
}
void pos2Callback(const nav_msgs::Odometry::ConstPtr& msg)
{
  pos2 = *msg;
}
int main(int argc, char **argv)
{
  ros::init(argc, argv, "rf_odom_pub");
  ros::NodeHandle n;
  ros::Subscriber sub1 = n.subscribe("/burger/odom", 500, pos1Callback);
  ros::Subscriber sub2 = n.subscribe("/waffle_pi/odom", 500, pos2Callback);
  ros::spinOnce();
  
  ros::Publisher pub1 = n.advertise<geometry_msgs::Point>("hps_pos", 1000);
  ros::Rate loop_rate(10);
  geometry_msgs::Point posmark;
  std::srand(time(0));

  posmark.x = -2;
  posmark.y = -2;
  int count = 0;
  while (ros::ok())
  {
    double robot1 = pos1.pose.pose.position.x + pos1.pose.pose.position.y + 6;
    double robot2 = pos2.pose.pose.position.x + pos2.pose.pose.position.y + 6;
    double max_x = posmark.x + 0.1;
    double min_x = posmark.x - 0.1;
    double max_y = posmark.y + 0.1;
    double min_y = posmark.y - 0.1;
    double bananas = posmark.x + posmark.y;

    if (pos1.pose.pose.position.x <= max_x && pos1.pose.pose.position.x >= min_x)
    {
      if (pos1.pose.pose.position.y <= max_y && pos1.pose.pose.position.y >= min_y){
        posmark.x = posmark.x + 1.75;
        posmark.y = posmark.y + 1.49;
      }
    }
    if (pos2.pose.pose.position.x <= max_x && pos2.pose.pose.position.x >= min_x)
    {
      if (pos2.pose.pose.position.y <= max_y && pos2.pose.pose.position.y >= min_y){
        posmark.x = posmark.x + 1.21;
        posmark.y = posmark.y + 1.35;
      }
    }

    ROS_INFO("\nClock:\t%i\nPosition Mark:\n\tx:%f\n\t\tMax X:%f\n\t\tMin X:%f\n\ty:%f\n\t\tMax Y:%f\n\t\tMin Y:%f\n\tz:%f\nPosition Robot 1:\n\tx:%f\n\ty:%f\nPosition Robot 2:\n\tx:%f\n\ty:%f\nR1:%f\tR2:%f", count, posmark.x, max_x, min_x, posmark.y, max_y, min_y, posmark.z, pos1.pose.pose.position.x, pos1.pose.pose.position.y, pos2.pose.pose.position.x, pos2.pose.pose.position.y, robot1, robot2);
    
    pub1.publish(posmark);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}