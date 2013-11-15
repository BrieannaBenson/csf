# Name: Brieanna Benson
# Evergreen Login: benbri03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

names = dict()
names['Brieanna'] = 'Fresno'
names['Nicolas'] = 'Olympia'
for value in names.itervalues():
    print value
names['Rayne'] = 'San Jose'
names['Ronald'] = 'Eureka'
names['Lisa'] = 'Bellingham'
names['Bill'] = 'New York'
del names['Brieanna']
del names['Nicolas']

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

mammals = []
mammals.append('cat')
mammals.append('dog')
mammals.append('elephant')
for value in mammals:
    print value

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

def printlist(stuff):
    for i in stuff:
        print i
sandwich = ['rubin', 'BLT', 'burger']
capitals = ['Paris', 'Berlin', 'Tokyo']
printlist(sandwich)
printlist(capitals)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

test1 = {'Person': 'John', 'Midterm': 78, 'Final': 89}
test2 = {'Person': 'Jane', 'Midterm': 97, 'Final': 67}
test3 = {'Person': 'Jacob', 'Midterm': 82, 'Final': 84}
test4 = {'Person': 'Jay', 'Midterm': 56, 'Final': 99}
Test_Scores = [test1, test2, test3, test4]

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

for i in Test_Scores:
    name = i['Person']
    midterm = i['Midterm']
    final = i['Final']
    print "The difference between " + name + "'s scores is: " + str(abs(midterm - final))

###
### Collaboration
###

# Nick Mendelson