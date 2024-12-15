# Robotic Arm Maze Solver with Digital Twin and Physical Execution

## Project Overview
This project integrates robotics, computer vision, and path planning to enable a MyCobot Pro 600 robotic arm to autonomously navigate a 4x4 maze. The project uses MATLAB and Python for modeling, kinematics, and real-world control. Key components include a digital twin, real-time mapping from camera inputs to physical coordinates, and seamless robot motion control via joint angle computation.

## Features
- **Digital Twin Simulation**: A URDF model of the MyCobot Pro 600 robotic arm for kinematic simulation in MATLAB.
- **Coordinate Mapping**: Camera-based detection of ArUco markers for mapping pixel coordinates to physical coordinates.
- **Path Planning**: Implementation of the Breadth-First Search (BFS) algorithm to find the shortest maze solution.
- **Inverse Kinematics**: MATLAB's Robotics Toolbox calculates joint angles to achieve target end-effector positions.
- **Physical Robot Control**: Python script sends computed joint angles to the robotic arm via a TCP connection.
- **Automation**: Excel sheets serve as the central data exchange for calibration parameters, pixel-to-physical coordinate mapping, and joint angles.

## System Workflow
1. **Calibration**:
   - Detect ArUco markers to calculate linear mapping parameters (mx, cx, my, cy).
   - Save calibration parameters to `Project_parameters_file.xlsx` under the `calibration_parameters` sheet.

2. **Maze Solving**:
   - Capture the maze image and detect solution points.
   - Save interpolated pixel coordinates to the `Pixel_coordinates` sheet.
   - Compute physical coordinates using calibration parameters and save them to the `physical_coordinates` sheet.

3. **Joint Angle Calculation**:
   - Use MATLAB's inverse kinematics function through Python's MATLAB engine.
   - Joint angles are saved in the `Joint_angles` sheet.

4. **Robot Motion**:
   - Apply the computed joint angles to both the digital twin and the physical robot.
   - Verify successful maze traversal through animation and real-world execution.

## Prerequisites
- **Software**:
  - MATLAB (with Robotics Toolbox and MATLAB Engine API for Python).
  - Python 3.x.
  - Required Python libraries: `pandas`, `openpyxl`, `socket`, `numpy`.
- **Hardware**:
  - MyCobot Pro 600 robotic arm.
  - AI Kit camera for visual input.

## Setup
1. Clone the repository:
   ```bash
   git clone repository_url](https://github.com/Devika-S-N/Maze-Solving-with-Mycobot-Pro-600
   cd Maze-Solving-with-Mycobot-Pro-600
   ```
2. Install Python dependencies:
   ```bash
   pip install pandas openpyxl numpy
   ```
3. Set up MATLAB Engine for Python by following [MathWorks documentation](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html).
4. Configure the robot's TCP/IP connection as per the [MyCobot Pro 600 API guide](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.3-myCobot_Pro_600/2.3.5%20socket%20API%20interface%20description.html).

## Usage
### Step 1: Calibration
Run the Python script to detect ArUco markers and save calibration parameters:
```bash
python detect_aruco_calibration.py
```

### Step 2: Maze Solving
Run the maze-solving script to calculate pixel and physical coordinates:
```bash
python maze_solver.py
```

### Step 3: Joint Angle Calculation
Use the MATLAB-Python interface to calculate joint angles:
```bash
python compute_joint_angles.py
```

### Step 4: Physical Robot Execution
Run the robot control script to send joint angles to the robot:
```bash
python control_robot.py
```

### Step 5: Verification with Digital Twin
Run the MATLAB script for digital twin animation:
```matlab
run('digital_twin_simulation.m')
```

## Results
- Both the digital twin and the physical robot successfully navigated the maze without errors.
- The verification underscores the accuracy and precision of the system.

## Repository Structure
```
├── README.md
├── detect_aruco_calibration.py
├── maze_solver.py
├── compute_joint_angles.py
├── control_robot.py
├── digital_twin_simulation.m
├── Project_parameters_file.xlsx
├── urdf/
│   └── my_pro600.urdf
└── resources/
    ├── calibration_plate.png
    └── maze_image.png
```

## References
1. Elephant Robotics, "Socket API Interface Description for myCobot Pro 600," Available: [Socket API](https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.3-myCobot_Pro_600/2.3.5%20socket%20API%20interface%20description.html).
2. MathWorks, "MATLAB Engine for Python," Available: [MATLAB Engine](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html).
3. MathWorks, "TCP/IP Communication," Available: [TCP/IP Communication](https://www.mathworks.com/help/matlab/matlab-engine/tcp-ip-communication.html).
4. MathWorks, "GeneralizedInverseKinematics System Object," Available: [Generalized Inverse Kinematics](https://www.mathworks.com/help/robotics/ref/generalizedinversekinematics-system-object.html).
5. GeeksforGeeks, "Breadth First Search or BFS for a Graph," Available: [BFS Guide](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/).

## License
This project is licensed under the MIT License. See `LICENSE` for details.

