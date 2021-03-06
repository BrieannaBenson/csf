# Name: Brieanna Benson
# Evergreen Login: benbri03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

# stores the three individual values for a, b, and c in the quadratic function, specifically that of the equation (x^2 - 5.86x + 8.5408)
matha = 1
mathb = -5.86
mathc = 8.5408

# calculates and stores the root values of the equation once passed through the quadratic function
root1 = ((mathb* -1) + math.sqrt((mathb**2) + (4*matha*mathc)))/(2*matha)
root2 = ((mathb* -1) - math.sqrt((mathb**2) + (4*matha*mathc)))/(2*matha)

# convert floats to strings
result1 = str(root1)
result2 = str(root2)

# prints the resulting roots
print 'The roots are: ' + result1 + ' and ' + result2

###
### Problem 2
###

print "Problem 2 solution follows:"

# loads the file into a variable
import hw1_test

# assign values from hw1_test to variables
a = hw1_test.a
b = hw1_test.b
c = hw1_test.c
d = hw1_test.d
e = hw1_test.e
f = hw1_test.f

# print each value
print 'a = ' + str(a)
print 'b = ' + str(b)
print 'c = ' + str(c)
print 'd = ' + str(d)
print 'e = ' + str(e)
print 'f = ' + str(f)
               
###
### Problem 3
###

print "Problem 3 solution follows:"

# creates a boolean variable based on the result of the expression given
boolresult = ((a and b) or (not c) and not (d or e or f))

# prints the value as a string
print str(boolresult)

# REFLECTION: This assignment took m about 3 hours to complete.  With the sufficent resources available in the textbook and via testing in Repl,it, I was able to complete most of this assignment with little trouble.