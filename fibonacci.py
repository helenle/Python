import math

# fibonacci
def fibonacci(n):
	if not isinstance(n, int):
		print "fibonacci is only defined for integers."
		return -1
	elif n < 0:
		print "fibonacci is only defined for positive integers."
		return -1
    elif 0 <= n <= 1: # or if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)  
    
print 'fibonacci =', fibonacci(5)
