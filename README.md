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
* Jupyter Notebook (`main.ipynb`)
* Custom Python Packages (`seating_plan` and `tests`)

## Steps to Install & Run the Project
1. Prerequisites: Make sure you have Python and Jupyter Notebook installed on yur computer(or use an environment like Anaconda or Google Colab).
2. Download or clone the project repository containing the project files (`main.ipynb`, the `seating_plan/` directory, and the `tests/` directory).
3. Launch Jupyter Notebook or JupyterLab on your computer.
4. Open the `main.ipynb` notebook.
5. Run the code cells sequentially to input student lists, define grid dimensions, generate the seating plan, and view total branch clashes.

## Instructions for Testing
1. Locate the testing section within `main.ipynb` or open the `tests/test_collisions.py` file.
2. Run the test execution cell (`run_tests()`) to simulate a test grid configuration.
3. Verify that the system successfully asserts the test conditions, outputting `SUCCESS: Collision test passed successfully!`.

## Screenshots
It's been provided in the project pdf. 
