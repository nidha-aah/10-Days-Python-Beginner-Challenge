# Bill split calculator

print("Bill split calculator")

bill = float(input("What was the total bill? "))
tip_percent = float(input("What percentage tip would you like to give? "))
people = int(input("How many people are splitting the bill? "))

tip = bill * tip_percent / 100
total_bill = bill + tip
each_person = total_bill / people


print("\n----- Bill Summary -----")
print("Bill:", bill)
print("Tip:", tip)
print("Total Bill:", total_bill)
print("Each person should pay:", each_person)