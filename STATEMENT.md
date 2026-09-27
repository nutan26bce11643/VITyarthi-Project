# Project Statement: Exam Seating Matrix and Branch Collision Checker

## Problem Statement
For conducting examinations, it is important to ensure that students from the same academic branch are not seated right next to each another to minimize the risk of any malpractice. Manually creating a seating matrix plan and counting these branch clashes for a large number of students is inefficient,time taking and prone to error. There is a need for a programmatic tool that can arrange students in a matrix and automatically calculate the number of adjacent same-branch seating clashes quickly.

## Scope of the Project
This program takes list of student records and sequentially arrange them into a two-dimensional grid representing a classroom of defined rows and columns. Once the seats are filled, it checks the seating arrangement by examining adjacent seats to the right and directly below to find any matching branches. It outputs the visual final classroom seating plan and a final count of total branch clashes.

## Target Users
* Exam Invigilators
* University Administration Staff
* University Examination Coordinators

## High-Level Features
1. **Sequential Grid Allocation:** Fills a classroom matrix automatically row by row using students data from the list provided .
2. **Collision Detection:** Evaluates adjacent seat coordinates to detect any matching academic branches between neighbouring seats.
3. **Layout display:** Prints a clean, text-based layout of the exam hall seating arrangement for easy verification.
