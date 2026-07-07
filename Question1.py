# python ro classify a studemt's grade

score1 = float(input("Enter score for Course 1: "))
score2 = float(input("Enter score for course 2: "))
score3 = float(input("Enter score fot course 3: "))
score4 = float(input("Enter score for course 4: "))
score5 = float(input("Enter score for course 5: "))

# Calculate the average score
average = (score1 + score2 + score3 + score4 + score5) /5

# Determine the grade
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 45:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade ="F"

#Display the results
print("\n----- STUDENT RESULT -----")
print("course 1 score:", score1)
print("course 2 score:", score2)
print("course 3 score:", score3)
print("course 4 score:", score4)
print("course 5 score:", score5)
print("average score:", average)
print("Grade:", grade)

# Demonstrating Python Data Structures

# List
Courses = ("Python", "Mathematics", "Statistics")
print("list:", Courses)

# Tuple
Colors =("Red", "Blue", "Green")
print("Tuple:", Colors)

# Dictionary
Student = {
    "Name":"John",
    "Age": 20,
    "Department": "Data Science and Analytics"

}
print("Dictionary:", Student)

# Set
numbers = {10, 20, 30, 40, 50}
print("set:", numbers)

# Demonstrating Type Conversion

# Integer
num1 =50

# Convert Integer to Float
float_num = float(num1)
print("Integer to Float:", float_num)

# Float
num2 = 25.75

# Convert Float to String
string_num = str(num2)
print("Float to String:", string_num)

# String
num3 = "100"

# Convert String to Integer
int_num = int(num3)
print("String to Integer:", int_num)

# Program to print prime numbers from 1 to 100

print("Prime numbers between 1 and 100 are:")

for num in range(2,101):
    for i in range(2, num):
        if num % i ==0:
            break
    else:
        print(num)

    
