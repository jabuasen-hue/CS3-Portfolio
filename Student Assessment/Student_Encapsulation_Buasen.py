class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age
        self.__grade = grade

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age!")

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

student1 = Student("Alex", 15, 90)
print("Original Student Information")
print("Name:", student1.name)
print("Age:", student1.get_age())
print("Grade:", student1.get_grade())

student1.set_age(16)
print("\nTest 1 - Age:", student1.get_age())
student1.set_age(-5)
print("Test 2 - Age:", student1.get_age())

student1.set_grade(95)
print("\nTest 3 - Grade:", student1.get_grade())
student1.set_grade(150)
print("Test 4 - Grade:", student1.get_grade())
student1.set_grade(0)
print("\nTest 5 - Grade:", student1.get_grade())