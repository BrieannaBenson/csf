# Name: Brieanna Blue Benson
# Evergreen Login: benbri03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

# imports a file's values
import hw2_test

# sets storage space for the value a as n from the file and a value of 10 to the n here
a = hw2_test.n
n = 10

# creates a list based on the n values desired to divide 1 by
numbers = []
x = 1
while x <= n:
    numbers.append(x)
    x += 1

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# declares space for the sum, start value, and end value that was imported
sum = 0
x = 1

# loops through, adding i to sum and incrementing it until it is above n's value
while x <= a:
    sum += x
    x += 1
print str(sum)
    
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# takes each number from the list, divides 1 by it, then prints the result until the list is exhausted
for x in numbers:
    decresult = (1.0/x)
    print decresult

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

# creates space to sum up the number
triangular = 0

# uses the previous question's list of 1 to 10 and adds each to the sum value
for x in numbers:
    triangular += x

# prints results, the second after puting n through an equation
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# sets starting product
product = 1

# multiplies each number from 1 to 10
for x in numbers:
    product *= x

# prints the result
print "The factorial for", n, "is", product

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# makes a reference variable to the main list, a number of lines to print, and a space for the result of the factoiral
factorials = numbers
nlines = n
result = 1

# loops through the amount of lines/factorials desired to solve, changes the list of factorials to the next desired values
while nlines > 0:
    
    # multiplies all the numbers in the list to form the result
    for x in factorials:
        result *= x
    
    print result
    nlines -= 1
    del factorials[len(factorials)-1]
    result = 1

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# resets the values for the main list
x = 1
while x <= n:
    numbers.append(x)
    x += 1

# makes a reference variable to the main list, a number of lines to print, and a space for the result of the factoiral, makes storage for the total of the factorials
recipfacts = numbers
nnumbers = n
recipresult = 1
total = 1

# loops through the amount of lines/factorials desired to solve, changes the list of factorials to the next desired values, adds to the total
while nnumbers > 0:
    
    # multiplies all the numbers in the list to form the result    
    for x in recipfacts:
        recipresult *= x
    
    total += (1.0/recipresult)
    nnumbers -= 1
    del recipfacts[len(recipfacts)-1]
    recipresult = 1

# prints the total value
print total

###
### Collaboration
###

# Repl,it: Used this site to test each problem's code and test other functions to see if they had applicible use in the program

###
### Reflection
###

# This assignment took me about 5 hours to complete, including the readings
