import math

def printLogarithm(x):
    if x <= 0:
        print "Positive numbers only, please."
        return
    
    result = math.log(x)
    print "The log of x is", result
    
printLogarithm(-10)    

def countdown(n):
    if n == 0:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)

countdown(5)

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
#        recursive = factorial(n-1)
#        result = n * recursive
#        print result
#        return result
# OR one statement below to return result
        return n * factorial(n-1)  # Can't use print, though
             
print 'Factory of 5! =', factorial(5)
