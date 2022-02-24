class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 to 100
    
    def get_grade(self):
        return self.grade
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)

s1 = Student("Ishant", 19, 95)
s2 = Student("Ramesh", 18, 75)
s3 = Student("Mukhesh", 20, 66)

ScienceCourse = Course("Science", 2)
ScienceCourse.add_student(s1)
ScienceCourse.add_student(s2)
print(ScienceCourse.add_student(s3))
print(ScienceCourse.students[0].name)
print(ScienceCourse.get_avg_grade())