class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("print new student in Database ")

s1= Student("Ehsanul")
print(s1.name)