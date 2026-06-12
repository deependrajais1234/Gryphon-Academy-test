
language= {"Python", "Java", "C++", "Python", "Java", "C"}
print(language)

language_2 = {"Python", "JavaScript", "C"}
print(language_2)


print(language.union(language_2))

print(language.intersection(language_2))


print(language.difference(language_2))


# Tuple Operations

cities = ("Bhopal", "Delhi", "Mumbai", "Bhopal", "Pune")


print(cities)
print(cities.count("Bhopal"))


print(cities.index("Mumbai"))

if "Delhi" in cities:
    print("Delhi is present in tuple")
else:
    print("Delhi is not present")


try:
    cities[0] = "Indore"
except TypeError:
    print("Tuple cannot be modified")