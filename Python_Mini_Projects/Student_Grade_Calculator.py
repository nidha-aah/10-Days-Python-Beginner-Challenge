sub1 = int(input("Enter Python marks: "))
sub2 = int(input("Enter SQL marks: "))
sub3 = int(input("Enter ML marks: "))

print (f"python mark: {sub1}")
print(f"SQL mark: {sub2}")
print(f"ML mark: {sub3}")

total_mark = sub1 + sub2 + sub3
print(f"Total mark: {total_mark}")

avg_mark = total_mark / 3
print(f"Average mark: {round(avg_mark,2)}")


if 90 <= avg_mark <= 100:
    print("Grade : A+")
elif 80 <= avg_mark <= 89:
    print("Grade : A")
elif 70 <= avg_mark <= 79:
    print("Grade : B")
elif 60 <= avg_mark <= 69:
    print("Grade : C")
else:
    print("Grade : D")
