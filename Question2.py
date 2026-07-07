# question 1
try:
    file = open(r"C:\Users\SEDATECH\Desktop\PYTHON FILES\student. txt.txt", "r")
    content = file.read()
    file.close()

    words = content.split()
    word_count = len(words)

    result = open("result.txt", "w")
    result.write("Number of words: " + str(word_count))
    result.close()

    print("Word Count:", word_count)
    print("Result has been written to result.txt")

except FileNotFoundError:
    print("File not found.")

# question 2
# class student

class student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 45:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "F"

student1 = student("John", "DS001", 85)

print("Name:", student1.name)
print("Roll Number:", student1.roll_number)
print("Marks:", student1.marks)
print("Grade:", student1.calculate_grade())

# question 3
# Parent class
class student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks


    def calculate_grade(self):
        if self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 45:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "F"

# Child class
class GraduateStudent(student):

    def __init__(self, name, roll_number, marks, research_topic):
        super().__init__(name, roll_number, marks)
        self.research_topic = research_topic

student1 = GraduateStudent(
    "John",
    "DS001",
    85,
    "Artificial Intelligence"
)

print("Name:", student1.name)
print("Roll Number:", student1.roll_number)
print("Marks:", student1.marks)
print("Research Topic:", student1.research_topic)
print("Grade:", student1.calculate_grade())
    
        
    


