import sys

class Teacher:
   def __init__(self, data):
      self.tLastName = data[0].strip()
      self.tFirstName = data[1].strip()
      self.classroom = data[2].strip()

   def matchedByClassroom(self, classroom):
      return self.classroom == classroom

   def matchedBytLastName(self, lastname):
      return self.tLastName == lastname

   def __str__(self):
      return self.tLastName + "," + self.tFirstName

class Student:
   def __init__(self, data):
      self.stLastName = data[0].strip()
      self.stFirstName = data[1].strip()
      self.grade = data[2].strip()
      self.classroom = data[3].strip()
      self.bus = data[4].strip()
      self.gpa = data[5].strip()

   def matchedByStLastName(self, lastname):
      return self.stLastName == lastname

   def matchedByClassroom(self, classroom):
      return self.classroom == classroom

   def matchedByBus(self, bus):
      return self.bus == bus

   def matchedByGrade(self, grade):
      return self.grade == grade

   def __str__(self):
      return self.stLastName + "," + self.stFirstName + "," + self.grade + "," + self.classroom + "," + self.bus + "," + self.gpa


def print_info(students):
   info = dict()
   for student in students:
      grade = int(student.grade)
      if grade in info:
         info[grade] += 1
      else:
         info[grade] = 1
   keys = sorted(info.keys())
   for i in keys:
      print("{0}: {1}".format(i, info[i]))

def calc_total_students_by_classroom(students):
   data = dict()
   for student in students:
      classroom = int(student.classroom)
      if classroom in data:
         data[classroom] += 1
      else:
         data[classroom] = 1
   keys = sorted(data.keys())
   for i in keys:
      print("{0}: {1}".format(i, data[i]))


def student_list_of_grade(grade, students):
   results = []
   for student in students:
      if student.matchedByGrade(grade):
         results.append(student)
   return results

def find_teacher_by_classroom(teachers, classroom):
   results = []
   for teacher in teachers:
      if teacher.matchedByClassroom(classroom):
         results.append(teacher)
   return results

def analyze_grade(students, teachers, grade):
   results = []
   for student in students:
      if student.matchedByGrade(grade):
         results.append(student)
   for student in results:
      teachers_found = find_teacher_by_classroom(teachers, student.classroom)
      for teacher in teachers_found:
         print(student.gpa + "," + student.bus + "," + teacher.tLastName + "," + teacher.tFirstName)

def analyze_teacher(students, teachers, tLastName):
   teachers_found = []
   for teacher in teachers:
      if teacher.matchedBytLastName(tLastName):
         teachers_found.append(teacher)
   for teacher in teachers_found:
      for student in students:
         if student.matchedByClassroom(teacher.classroom):
            print(student.gpa + "," + student.bus + "," + teacher.tLastName + "," + teacher.tFirstName)

def analyze_bus(students, teachers, bus):
   for student in students:
      if student.matchedByBus(bus):
         teachers_found = find_teacher_by_classroom(teachers, student.classroom)
         for teacher in teachers_found:
            print(student.gpa + "," + student.bus + "," + teacher.tLastName + "," + teacher.tFirstName)

def analyze_performance(students, teachers, inputs):
   params = inputs.strip().split(" ")
   params[0] = params[0].strip()
   params[1] = params[1].strip()
   if params[0] == 'G' or params[0] == 'Grade':
      analyze_grade(students, teachers, params[1])
   elif params[0] == "T" or params[0] == "Teacher":
      analyze_teacher(students, teachers, params[1])
   elif params[0] == "B" or params[0] == "Bus":
      analyze_bus(students, teachers, params[1])

def main():
   students = []
   teachers = []
   f = open("list.txt", "r")
   f1 = open("teachers.txt", "r")
   for line in f:
      line = line.strip()
      data = line.split(",")
      student = Student(data)
      students.append(student)
   for line in f1:
      line = line.strip()
      data = line.split(",")
      teacher = Teacher(data)
      teachers.append(teacher)
   f.close()
   for line in sys.stdin:
      line = line.strip()
      if line == "Q" or line == "Quit":
         break
      elif line == "I" or line == "Info":
         print_info(students)
      elif line == "E" or line == "Enrollment":
         calc_total_students_by_classroom(students)
      else:
         inputs = line.split(":")
         if len(inputs) <= 1:
            continue
         if inputs[0] == "S" or inputs[0] == "Student":
            tmp = inputs[1].strip()
            params = tmp.split(" ")
            lastname = params[0].strip()
            bus = False
            if len(params) > 1:
               if params[1].strip() == "B" or params[1].strip() == "Bus":
                  bus = True
            found = 0
            for student in students:
               if student.matchedByStLastName(lastname):
                  found += 1
                  teachers_found = find_teacher_by_classroom(teachers, student.classroom)
                  if bus == False:
                     for teacher in teachers_found:
                        print(student.stLastName + "," + student.stFirstName + "," + student.grade + "," + student.classroom + "," + teacher.tLastName + "," + teacher.tFirstName)
                  else:
                     print(student.stLastName + "," + student.stFirstName + "," + student.bus)
            if found == 0:
               print()
         elif inputs[0] == "T" or inputs[0] == "Teacher":
            lastname = inputs[1].strip()
            found = 0
            classroom = ""
            for teacher in teachers:
               if teacher.matchedBytLastName(lastname):
                  classroom = teacher.classroom
                  break
            for student in students:
               if student.matchedByClassroom(classroom):
                  found += 1
                  print(student.stLastName + "," + student.stFirstName)
            if found == 0:
               print()
         elif inputs[0] == "B" or inputs[0] == "Bus":
            bus = inputs[1].strip()
            for student in students:
               if student.matchedByBus(bus):
                  print(student.stFirstName + "," + student.stLastName + "," + student.grade + "," + student.classroom)
         elif inputs[0] == "G" or inputs[0] == "Grade":
            tmp = inputs[1].strip()
            params = tmp.split(" ")
            grade = params[0].strip()
            results = student_list_of_grade(grade, students)
            if len(params) > 1 and len(results) > 0:
               def f(s): return float(s.gpa)
               student = None
               if params[1].strip() == "T" or params[1].strip() == "Teacher":
                  classrooms = set()
                  for student in students:
                     if student.matchedByGrade(grade):
                        classrooms.add(student.classroom.strip())
                  for classroom in classrooms:
                     for teacher in teachers:
                        if teacher.matchedByClassroom(classroom):
                           print(teacher)
                  continue
               elif params[1].strip() == "H" or params[1].strip() == "High":
                  student = max(results, key=f)
               elif params[1].strip() == "L" or params[1].strip() == "Low":
                  student = min(results, key=f)
               if student:
                  teachers_found = find_teacher_by_classroom(teachers, student.classroom)
                  for teacher in teachers_found:
                     print(student.stLastName + "," + student.stFirstName + "," + student.gpa + "," + teacher.tLastName + "," + teacher.tFirstName + "," + student.bus)
            else:
               if len(results) == 0:
                  print()
               for student in results:
                  print(student.stLastName + "," + student.stFirstName)
         elif inputs[0] == "A" or inputs[0] == "Average":
            grade = inputs[1].strip()
            results = student_list_of_grade(grade, students)
            if len(results) == 0:
               continue
            total = 0
            for student in results:
               total += float(student.gpa)
            print("{0},{1:.2f}".format(grade, (total / len(results))))
         elif inputs[0] == 'C' or inputs[0] == "Classroom":
            tmp = inputs[1].strip()
            params = tmp.split(" ")
            classroom = params[0].strip()
            if len(params) > 1:
               if params[1].strip() == "T" or params[1].strip() == "Teacher":
                  for teacher in teachers:
                     if teacher.matchedByClassroom(classroom):
                        print(teacher)
            else: 
               for student in students:
                  if student.matchedByClassroom(classroom):
                     print(student)
         elif inputs[0] == "P" or inputs[0] == "Performance":
            analyze_performance(students, teachers, inputs[1])


if __name__ == "__main__":
   main()
