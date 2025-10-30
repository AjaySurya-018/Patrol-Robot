# Patrolling Robot using ROS2 Navigation

> An autonomous patrol robot implementation for monitoring parking lot compliance using ROS2 Humble.

<img width="1373" alt="Patrol Robot Simulation" src="https://github.com/user-attachments/assets/db2f8ae1-380d-4aac-be49-e2a5c2b0aaa7" />

## Overview

This project implements an autonomous patrol robot capable of navigating a grocery store parking lot and detecting improperly parked vehicles. Built using ROS2 Humble, the system leverages SLAM for localization and Nav2 for autonomous navigation.

## Key Features

- **Custom Robot Design**: 2-wheel differential drive robot built with XACRO
- **Sensor Integration**: LIDAR and camera sensors for environment perception
- **Custom Environment**: Gazebo-simulated grocery store parking lot
- **SLAM Localization**: Real-time mapping and localization using SLAM Toolbox
- **Autonomous Navigation**: Nav2-based path planning with 2D goal pose control
- **Violation Detection**: Automated detection and reporting of parking violations

## System Architecture
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Gazebo    │────▶│  SLAM Toolbox│────▶│    Nav2     │
│ Simulation  │     │  (Mapping)   │     │ (Planning)  │
└─────────────┘     └──────────────┘     └─────────────┘
       │                    │                     │
       └────────────────────┴─────────────────────┘
                            │
                      ┌─────▼──────┐
                      │   RViz2    │
                      │(Visualization)
                      └────────────┘
```

## Technical Stack

- **ROS2**: Humble Hawksbill
- **Simulation**: Gazebo Classic
- **Visualization**: RViz2
- **Localization**: SLAM Toolbox
- **Navigation**: Nav2 Stack
- **Robot Description**: XACRO/URDF

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/Patrolling-Robot-using-ROS2-Navigation.git
cd Patrolling-Robot-using-ROS2-Navigation

# Build workspace
colcon build --symlink-install
source install/setup.bash
```

## Usage

### Launch Simulation
```bash
ros2 launch patrol_robot gazebo.launch.py
```

### Generate Map (SLAM)
```bash
ros2 launch patrol_robot slam.launch.py
```

### Autonomous Navigation
```bash
ros2 launch patrol_robot navigation.launch.py
```

Set navigation goals using the **2D Goal Pose** tool in RViz2.

## Functionality

The robot continuously patrols designated areas of the parking lot. When vehicles are detected in restricted zones:

- **Console Alert**: Violation message published to `/parking_violations`
- **Coordinate Logging**: Precise location (x, y, θ) of the violating vehicle
- **Real-time Monitoring**: Continuous surveillance during patrol routes

## Project Structure
```
patrol_robot/
├── config/          # Navigation and SLAM parameters
├── description/     # URDF/XACRO robot models
├── launch/          # Launch files
├── maps/            # Generated maps
├── worlds/          # Gazebo world files
└── src/             # Source code
```

## Dependencies

- `ros-humble-gazebo-ros-pkgs`
- `ros-humble-slam-toolbox`
- `ros-humble-navigation2`
- `ros-humble-nav2-bringup`
- `ros-humble-robot-state-publisher`

## Acknowledgments

Course: Robotic Operating Systems  
Institution: [Amrita University]
