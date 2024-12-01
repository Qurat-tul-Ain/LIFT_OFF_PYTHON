#Lift off counter

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Here's a sample run of the program:

# 10 9 8 7 6 5 4 3 2 1 Liftoff!

# There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. Recall that i will keep track of how many times the for loop has completed executing its body. As an example this code:

# for i in range(10): print(i)

# Will print out the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. The values printed in liftoff are 10 minus the number of times the for loop has completed.

#--------------------------------------------------------------------------------------------

# Loop : For
# List of range

def countdown1():
    for i in range(10):
        print(i, end =" ")
    print("lift off!")

countdown1() # This line calls the function after it's defined

# list and for loop
number_list :list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def countdown2():
    for i in number_list:
        print(i, end=" ")
    print("Lift Off!") # Fixed the typo here: pirnt -> print

countdown2()

count_till = 3
while True:
  print("Counting...", count_till)
  count_till = count_till -1

  if count_till == 0:
   break




