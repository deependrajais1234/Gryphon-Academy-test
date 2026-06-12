students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Amit": {"age": 19, "marks": 75}
}

print(students)

students["Sneha"] = {"age": 20, "marks": 92}

students["Amit"]["marks"] = 80
print(students)

del students["Rahul"]

if "Priya" in students:
    print("Priya exists")
else:
    print("Priya does not exist")

print("Keys:")
for i in students.keys():
    print(i)

print("Values:")
for i in students.values():
    print(i)

print("Items:")
for i in students.items():
    print(i)

names = list(students.keys())
print(names)