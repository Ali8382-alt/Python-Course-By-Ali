
# Function Definition with Parameters
def average(a=10,b=20):
    averageValue= (a+b)/2
    print(averageValue)


# Function Calling with Arguments 
average(5, 10)
average(7, 10)
average(80, 98)
average()

# Write a function show_age(name, age) that prints: "Ali Ansari is 24
# years old."

def show_age(name="Ali Ansari", age= 24):
    print(f"{name} is {age} years old")

show_age("Ali Ansari", 24)
show_age()
show_age("Anas", 19)
