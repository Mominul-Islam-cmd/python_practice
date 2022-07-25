class triangle:
    t1=""
    t2=""

    def __init__(self,t1,t2):
        self.t1=t1
        self.t2=t2
    def display(self):
        print(f"triangle:{0.5*self.t1*self.t2}")

a=triangle(4,5)
a.display()