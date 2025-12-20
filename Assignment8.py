# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Ahmed knows.

programmingList= ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programmingList))
# how to convert a list into set

programmingSet= set(programmingList)
print(type(programmingSet))
print(programmingSet)
print("Ahmed knows these many langauges", len(programmingSet))


