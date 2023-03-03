import math
class Student:
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
    def RollNumber(self,R1):
        print( "my RollNumber is {}".format(R1))
    def ClassRoom(self,room):
        print("my classroom is {}".format(room))
class Subject(Student):
    def __init__(self, name, age, dob,tamil,english,french,hindi):
        super().__init__(name, age, dob)
        self.tamil= tamil
        self.english= english
        self.french= french
        self.hindi = hindi
    @property
    def TotalMark(self):
        return(self.tamil+self.english+self.french+self.hindi)
    @property
    def AverAge(self):
        return((self.tamil+self.english+self.french+self.hindi)/4)
    def rank(self,grade):
        print("my grade is {}".format(grade))
# class Attendence(Subject):
#     def __init__(self, name, age, dob, tamil):
#obj=Student("RA2132003010025",23,12)
#         super().__init__(name, age, dob, tamil)
obj2=Subject(21,"Swetha","12/06/2001",52,58,78,55)
obj2.RollNumber("RA2132003010025")
obj2.ClassRoom("III - Year")
obj2.rank("O+")

classes= obj2.__class__

print("{} my name is {} my age is {} my dob is {} tamil mark {} english mark {} french mark {} hindi mark {} my total mark is {} average {}".format(classes.__name__,obj2.age,obj2.name,obj2.dob,obj2.tamil,obj2.english,obj2.french,obj2.hindi,obj2.TotalMark,math.ceil(obj2.AverAge)))