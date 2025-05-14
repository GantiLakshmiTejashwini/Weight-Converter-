# converter.py

def kg_to_pounds(kg):
return kg * 2.20462

def pounds_to_kg(lb):
return lb / 2.20462

print("1. Convert KG to Pounds")
print("2. Convert Pounds to KG")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
kg = float(input("Enter weight in kg: "))
print("Weight in pounds:", kg_to_pounds(kg))
elif choice == '2':
lb = float(input("Enter weight in pounds: "))
print("Weight in kg:", pounds_to_kg(lb))
else:
print("Invalid input")