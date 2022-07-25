class Student:
    ID=""
    CGPA=""

    def display(self):
        print(f"ID:{self.ID},CGPA:{self.CGPA}\n")
    def set_Value(self,roll,GPA):
        self.ID=roll
        self.CGPA=GPA

Mominul=Student()
Mominul.set_Value(121131,3.56)
Mominul.display()
Aminul=Student()
Aminul.set_Value(23112,3.45)
Aminul.display()