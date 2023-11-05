import datetime

class Student:
    name = ''
    birthyear = 2000
    grades = []
    group = ''

    def __init__(self, name, birthyear, grades, group):
        self.name = name
        self.birthyear = birthyear
        self.grades = grades
        self.group = group

    def get_gpa(self):
        return round(sum(self.grades) / len(self.grades), 1)

    def get_age(self):
        current_year = datetime.date.today().year
        age = current_year - self.birthyear
        return age

    def __str__(self):
        return  f' Student: {self.name}  |  God rojdeniya: {self.birthyear}  |  Godikov: {self.get_age()}  |  Sredniy bal: {self.get_gpa()}  |  Vse ocenki:{self.grades}  |  Gruppa: {self.group}'

students = [
    Student('Ivan', 2008, [10, 9, 10, 10, 8, 7], 'А'),
    Student('Maks', 2009, [8, 12, 10, 10, 8, 6], 'Б'),
    Student('Sergey', 2008, [8, 8, 11, 10, 8, 9], 'А'),
    Student('Egor', 2009, [9, 9, 10, 9, 8, 9], 'С'),
    Student('Oleg', 2010, [8, 9, 10, 10, 8, 10], 'Б')
]

for student in students:
    print(student)