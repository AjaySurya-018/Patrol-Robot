# Patrolling-Robot-using-ROS2-Navigation
This GitHub repo presents an end semester project submission for the course "Robotic Operating Systems" which showcasing the implementation of a Patrol Robot in ROS2 Humble distribution.

<img width="1373" height="862" alt="image" src="https://github.com/user-attachments/assets/db2f8ae1-380d-4aac-be49-e2a5c2b0aaa7" />


This project features the following :
***
 * Creation of a 2-Wheel Differential drive robot using xacro files
 * Integration of LIDAR sensor and camera into the robot's design
 * Generation of a Gazebo world, representing a parking lot of a Grocery store
 * Simulation of the robot within Gazebo through a launch file
 * Vizualization of the simulation in rviz 
 * Localization of the robot within the world by generating a map using Slam toolbox
 * Autonomous navigation of our robot in the world using 2D goal pose in rviz

## Functionality
The primary function of our robot is to patrol the parking lot of the Grocery store. In  cases where vehicles are improperly parked within prohibited areas, the robot prompts the user through console by publishing a message and also the coordinates of the wrongly parked vehicle.
