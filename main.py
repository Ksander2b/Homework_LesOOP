
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
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

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
lecturer_2.courses_attached += ['Python']


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

reviewer_2 = Reviewer('Benzhamin', 'Franklin')

student_1.rate_lecturer(lecturer_1, 'Python', 2)
student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 2)
student_1.rate_lecturer(lecturer_2, 'Python', 5)


student_2.rate_lecturer(lecturer_2, 'PHP', 2)
student_2.rate_lecturer(lecturer_2, 'PHP', 6)
student_2.rate_lecturer(lecturer_2, 'PHP', 2)

print(reviewer_1)
print(lecturer_1)
print(student_1)
is_lt = (student_2 > student_1)
print(is_lt)
is_lt_2 = (lecturer_1 < lecturer_2)
print(is_lt_2)


student_list = [student_1,student_2]  
print(student_1.grades)
print(student_2.grades)  

def intermediate_student_grade(list,cource_name):
    res = []
    for students in list:
        for keys, values in students.grades.items():
            if keys == cource_name:
                res += values
    res_final = sum(res)/len(res)
    return res_final

print(intermediate_student_grade(student_list, "C++"))

lecturer_list = [lecturer_1, lecturer_2]
print(lecturer_1.grades)
print(lecturer_2.grades)

def intermediate_lecturer_list(list,cource_name):
    res = []
    for lecturers in list:
        for keys, values in lecturers.grades.items():
            if keys == cource_name:
                res += values
    res_final = sum(res)/len(res)
    return res_final

print(intermediate_student_grade(lecturer_list, 'Python'))
