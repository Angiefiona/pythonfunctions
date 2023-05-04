class Student: 
    name = "Emily"
    age = 21
    school = "Akirachix"
    nationality = "Kenyan"
#instant variables
class Student:
    school = "Akirachix"
    def __init__(self, name, age, nationality):
       self.name =name
       self.age = age
       self.nationality = nationality
       #class method
    def greet_student(self):
        return  f"hello {self.name}, welcome {self.school},I am a {self.nationality}" 





