class phone:
    def message(self):
        print("Hi How are you")
    def price(self):
        print("20usd")
    def call(self):
        print("call me plz")
class iphone(phone):
    def emi_no(self):
        print("the number is not found")
    def inventor(self):
        print("this phone invent by usa")
a=iphone()
a.call()
a.emi_no()
a.price()
a.inventor()