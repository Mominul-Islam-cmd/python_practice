class Student:
    ID=""
    CGPA=""


    def __init__(self,roll,cgpa):
        self.ID=roll
        self.CGPA=cgpa

    def display(self):
        print(f"ID:{self.ID},cgpa:{self.CGPA}")

Momin= Student(123,3.54)
Momin.display()
Aminul=Student(213112,3.45)
Aminul.display()