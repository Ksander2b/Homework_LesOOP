
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self,course_name):
        self.finished_courses.append(course_name)
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        res = []
        for values in self.grades.values():
            res += values
        res_final = sum(res)/len(res)
        return res_final
    
    def __str__(self):
        joined_array = ', '.join(self.courses_in_progress)
        joined_array_2 = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашнее задание: {self.average_rate()}\nКурсы в процессе обучения: {joined_array}\nЗавершенные курсы: {joined_array_2}'
        return res

    def __lt__(self,other):
        return self.average_rate() < other.average_rate()
       

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
    
    def average_rate(self):
        res = []
        for values in self.grades.values():
            res += values
        res_final = sum(res)/len(res)
        return res_final
    
    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.average_rate()}'
        return res
    
    def __lt__(self,other):
        return self.average_rate() < other.average_rate()

class Reviewer (Mentor):
    
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}'
        return res
    



student_1 = Student('Alex', 'Bogatyrev', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JavaScript']
student_1.courses_in_progress += ['C++']

student_2 = Student('Misha', 'Bokarev', 'male')
student_2.courses_in_progress += ['JavaScript']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['PHP']

student_1.add_courses('Git')
student_2.add_courses('Python')

lecturer_1 = Lecturer('Adam', 'Smith')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Stive', 'Jobs')
lecturer_2.courses_attached += ['PHP']


reviewer_1 = Reviewer('Albert', 'Enshtain')
reviewer_1.courses_attached += ['C++']
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['PHP']
reviewer_1.courses_attached += ['JavaScript']
reviewer_1.rate_student(student_1, 'C++', 10)
reviewer_1.rate_student(student_1, 'C++', 4)
reviewer_1.rate_student(student_1, 'Python', 4)

reviewer_1.rate_student(student_2, 'JavaScript', 10)
reviewer_1.rate_student(student_2, 'C++', 4)
reviewer_1.rate_student(student_2, 'PHP', 6)

student_1.rate_lecturer(lecturer_1, 'Python', 2)
student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_2.rate_lecturer(lecturer_2, 'PHP', 2)
student_2.rate_lecturer(lecturer_2, 'PHP', 6)
student_2.rate_lecturer(lecturer_2, 'PHP', 2)

print(lecturer_1.grades)
print(student_1.grades)
print(lecturer_1)

print(student_1)
print(student_2.grades)

is_lt = (student_2 > student_1)
print(is_lt)

is_lt_2 = (lecturer_1 < lecturer_2)
print(is_lt_2)



# lecturer_Stiv = Lecturer('Stive', 'Jobs')
# print(lecturer_Stiv.name)




# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)