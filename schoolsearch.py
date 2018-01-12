import sys

class Student:
   def __init__(self, data):
      self.stLastName = data[0]
      self.stFirstName = data[1]
      self.grade = data[2]
      self.classroom = data[3]
      self.bus = data[4]
      self.gpa = data[5]
      self.tLastName = data[6]
      self.tFirstName = data[7]

   def matchedByStLastName(self, lastname):
      if self.stLastName == lastname:
         return True
      return False

   def matchedBytLastName(self, lastname):
      if self.tLastName == lastname:
         return True
      return False

   def matchedByBus(self, bus):
      if self.bus == bus:
         return True
      return False

   def matchedByGrade(self, grade):
      if self.grade == grade:
         return True
      return False

   def __str__(self):
      return self.stLastName + "," + self.stFirstName + "," + self.grade + "," + self.classroom + "," + self.bus + "," + self.gpa + "," + self.tLastName + "," + self.tFirstName

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

def student_list_of_grade(grade, students):
   results = []
   for student in students:
      if student.matchedByGrade(grade):
         results.append(student)
   return results

def main():
   students = []
   f = open("students.txt", "r")
   for line in f:
      line = line.strip()
      data = line.split(",")
      student = Student(data)
      students.append(student)
   f.close()
   for line in sys.stdin:
      line = line.strip()
      if line == "Q" or line == "Quit":
         break
      elif line == "I" or line == "Info":
         print_info(students)
      else:
         inputs = line.split(":")
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
                  if bus == False:
                     print(student.stLastName + "," + student.stFirstName + "," + student.grade + "," + student.classroom + "," + student.tLastName + "," + student.tFirstName)
                  else:
                     print(student.stLastName + "," + student.stFirstName + "," + student.bus)
            if found == 0:
               print()
         elif inputs[0] == "T" or inputs[0] == "Teacher":
            lastname = inputs[1].strip()
            found = 0
            for student in students:
               if student.matchedBytLastName(lastname):
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
               f = lambda s: float(s.gpa)
               student = None
               if params[1].strip() == "H" or params[1].strip() == "High":
                  student = max(results, key=f)
               elif params[1].strip() == "L" or params[1].strip() == "Low":
                  student = min(results, key=f)
               if student:
                  print(student.stLastName + "," + student.stFirstName + "," + student.gpa + "," + student.tLastName + "," + student.tFirstName + "," + student.bus)
            else:
               if len(results) == 0:
                  print()
               for student in results:
                  print(student.stLastName + "," + student.stFirstName)
         elif inputs[0] == "A" or inputs[0] == "Average":
            grade = inputs[1].strip()
            results = student_list_of_grade(grade, students)
            total = 0
            for student in results:
               total += float(student.gpa)
            print("{0},{1:.2f}".format(grade, (total/len(results))))

if __name__ == "__main__":
   main()
