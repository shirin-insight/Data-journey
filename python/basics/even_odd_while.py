# Exercise: Even or Odd Numbers
#
# Question:
# Use a while loop to print whether each number
# from 1 to 10 is even or odd.

number = 1

while number <= 10:
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

    number = number + 1