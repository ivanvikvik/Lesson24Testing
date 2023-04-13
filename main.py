class Student:
    def __init__(self, name='no name'):
        self.name = name

    # def __str__(self):
    #     return self.name


st = Student("Alex")
s = "Student: " + str(st)
print(s)
