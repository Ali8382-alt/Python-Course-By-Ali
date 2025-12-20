# Write a program to print the multiplication table of any number using a while
# loop.
# (Hint: Start i = 1 and run the loop until i <= 10.)
# Question 1:Loop to print multiplication table of 5 using for Loop
n=5
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

    

# Question 2: Loop to print multiplication table of 5 using while Loop
n=5
i= 1

while i<=10:
    print(f"{n} x {i} = {n*i} ")
    i+=1