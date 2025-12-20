# Dictionary Basics 

student= {
    "name": "Ali Ansari",
    "city": "Faisalabad",
    "age": 24,
    "rollNumber": 26,
}

print(type(student))
print(student["name"])
print(student)
print(student["city"])
# student["city"]= "Multan"
# print(student)
student["favSubject"]= "Maths"
print(student)
student.pop("favSubject")
print(student)
print(student.items())