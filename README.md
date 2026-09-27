# Project title- Exam Seating Matrix and Branch Collision Checker

## Overview of the project
This project is a Python-based program designed to arrange students into an exam hall seating matrix and count adjacent seat clashes between students belonging to the same academic branch. It processes a list of students, organizes them into a classroom grid, and evaluates the layout to prevent students from the same branch from sitting directly adjacent to one another,hence reducing the risk of any malpractice in examination hall.

## Features
* **Object-Oriented Data Structure:** Uses a dedicated `Student` class to securely manage student roll numbers, names, and branches
* **Matrix Allocation:** Initializes a 2D list grid based on classroom rows and columns, filling seats sequentially row by row while handling empty seats as "Empty".
* **Collision Detection Logic:** Traverses the matrix to evaluate adjacent right and bottom seats, tallying total branch clashes.
* **Formatted Display:** Outputs a clean, readable seating plan to the console.
* **Automated Unit Testing:** Includes a dedicated test script (`test_collisions.py`) to validate the accuracy of the collision counter.

## Technologies/Tools Used
* Programming language: Python 3.x
* Jupyter Notebook (`main.ipynb`) & Command-Line interface(`main.py`)
* Custom Python Packages (`seating_plan` and `tests`)

## Steps to Install & Run the Project
1. Prerequisites: Make sure you have Python installed on your computer along with the project files (`main.py`, `main.ipynb`, the `seating_plan/` directory, and the `tests/` directory).
2. Download or clone the project repository.
3. Open your command prompt or terminal and navigate to the `exam_seating_and_branch_collision_checker_project` folder.
4. Run the following command :
   ```bash
   python main.py

## Instructions for Testing
1. ​Execute python main.py in your command prompt.
2. The script will automatically output the seating plan, clash count, and run the automated test script (run_tests()).
3. Verify that the system outputs the success confirmation for the test suite i.e, `SUCCESS: Collision test passed successfully!`

## Screenshots
It's been provided in the project pdf. 
