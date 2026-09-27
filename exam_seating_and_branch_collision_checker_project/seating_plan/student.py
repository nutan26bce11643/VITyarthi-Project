# Class to store student details
class Student:
    def __init__(self, roll_no, name, branch):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch

    # Function to return student name and branch
    def get_info(self):
        return f"{self.name} ({self.branch})"