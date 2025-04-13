# class variable : Shared among all instance of a class
# defined outside the constructor
# allow you to share data among all objects created from the class . class variable also known as instance or global variable
class Student:
    classyear = 2024
    num_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students +=1

student1 = Student(f"spongebob",30)
student2 = Student(f"Patrick",20)
print(student1.name)
print(student2.age)
print(Student.classyear)
print(Student.num_students)
print(f"My graduating class of {Student.classyear} has {Student.num_students}")