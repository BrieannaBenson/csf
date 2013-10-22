# Brieanna Benson
# Lab 3
# Computer Science Foundations
# October 20th, 2013

# assign variables for 'if' check
n = 25
series = 'myon'

# steps to execute if the string is 'fibonacci'
if series == 'fibonacci':
    print 'Fibonacci numbers, the ' + str(n) + 'th fibonacci number'
    
    # create space for the ints to be counted
    totalints = n
    
    # create space for the proceeding two numbers, and the current fibonacci number
    x = 0
    y = 1
    z = 1
    
    # for each int, print the fibonacci number, then add to the next one, then set the proceeding values to the later two to be added in the next step
    for i in range(totalints):
        print z 
        z = x + y
        x = y
        y = z

# steps to execute if string is "sum"
elif series == 'sum':
    print 'The sum of the multiples of 3 up to 3 x ' + str(n)
    
    # create space to hold total value and the integer amount to incriment
    totalsum = 0
    intcount = n
    
    # incriment the addition of multiples of 3
    while intcount > 0:
        totalsum += (3*intcount)
        intcount -= 1
    
    # print the total
    print totalsum

# steps to execute if another value is entered for the string
else:
    print '"' + series +'" is not a valid choice.  Please enter either "fibonacci" or "sum".'
