class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_grades(self):
        return sum(sum(values) for values in self.grades.values()) / sum(
            len(values) for values in self.grades.values())

    def __lt__(self, other):
        return self.av_grades() < other.av_grades()

    def __gt__(self, other):
        return self.av_grades() > other.av_grades()

    def __eq__(self, other):
        return self.av_grades() == other.av_grades()

    def __ne__(self, other):
        return self.av_grades() != other.av_grades()

    def __le__(self, other):
        return self.av_grades() <= other.av_grades()

    def __ge__(self, other):
        return self.av_grades() >= other.av_grades()

    def __str__(self):
        course_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        av_grade = sum(sum(values) for values in self.grades.values()) / sum(
            len(values) for values in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {av_grade:.1f}\n"\
               f"Курсы в процессе изучения: {course_in_progress}\n" \
               f"Завершенные курсы: {finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def av_grades(self):
        return sum(sum(values) for values in self.grades.values()) / sum(
            len(values) for values in self.grades.values())

    def __lt__(self, other):
        return self.av_grades() < other.av_grades()

    def __gt__(self, other):
        return self.av_grades() > other.av_grades()

    def __eq__(self, other):
        return self.av_grades() == other.av_grades()

    def __ne__(self, other):
        return self.av_grades() != other.av_grades()

    def __le__(self, other):
        return self.av_grades() <= other.av_grades()

    def __ge__(self, other):
        return self.av_grades() >= other.av_grades()

    def __str__(self):
        grade = sum(sum(values) for values in self.grades.values()) / sum(
            len(values) for values in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grade:.1f}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student1 = Student('Глеб', 'Семенов', 'м')
student2 = Student('Ангелина', 'Иванова', 'ж')
lecturer1 = Lecturer('Максим', 'Смирнов')
lecturer2 = Lecturer('Валентина', 'Павлова')
reviewer1 = Reviewer('Андрей', 'Попов')
reviewer2 = Reviewer('Анна', 'Владимирова')

student1.courses_in_progress.append('Python')
student2.courses_in_progress.append('Java')

lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Git')
lecturer2.courses_attached.append('Python')
lecturer2.courses_attached.append('Java')

reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Java')

student1.finished_courses.append('Computer Science')
student2.finished_courses.append('Python Core')

reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 7)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Git', 8)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
