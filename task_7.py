import os


f = open("employees.txt", "w")

f.write("Rahul\n")
f.write("Amit\n")
f.write("Priya\n")

f.close()

print("Old Employee List")


f = open("employees.txt", "r")

for x in f:
    print(x)

f.close()

f = open("employees.txt", "a")

f.write("Rohan\n")
f.write("Sneha\n")

f.close()

print("New Employee List")


f = open("employees.txt", "r")

for x in f:
    print(x)

f.close()


os.remove("employees.txt")


if os.path.exists("employees.txt"):
    print("File is Present")
else:
    print("File Deleted")