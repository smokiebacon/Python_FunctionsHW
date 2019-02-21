class Member():
    def __init__(self, full_name):
        self.full_name = full_name
    
    def introduce(self):
        print(f'Hi, my name is {self.full_name}. Nice to meet you')


class Student(Member):
    def __init__(self, full_name, reason):
        Member.__init__(self, full_name)
        self.reason = reason

    def introduce(self):
        print(f'Hi, my name is {self.full_name}. I am here because {self.reason}')



class Teacher(Member):
    def __init__(self, full_name, bio):
        Member.__init__(self, full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skills):
        self.skills.append(skills)
    
    def introduce(self):
        print(f'Hi, my name is {self.full_name}. Bio {self.bio}. My skills are {self.skills}')


class Workshop():
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
    
    def add_participant(self, member):
        if type(member) == Student:
            self.students.append(member)
        else:
            self.instructors.append(member)
    
    def print_details(self):
        print(f'Workshop date: {self.date}. Subject: {self.subject}.')
        print('Instructors: ')
        for index, instructor in enumerate(self.instructors):
            print(index, instructor.full_name, instructor.bio)
        print('Students: ')
        for index, student in enumerate(self.students):
            print(index, student.full_name, student.reason)




jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Teacher("Vicky Lee", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Teacher("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop = Workshop("2/23/2019", "Web Dev")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)

workshop.print_details()