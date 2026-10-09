# Student Marks Analyzer

print("📊 Student Marks Analyzer")

students = []
marks_list = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    students.append(name)
    marks_list.append(marks)

print("\n--- Student Results ---")

for i in range(n):
    print(students[i], ":", marks_list[i])

total = sum(marks_list)
average = total / n
highest = max(marks_list)
lowest = min(marks_list)

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)