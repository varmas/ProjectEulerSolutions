import time

def max (a,b):
	
	if (a>b):
		return a
	
	return b
	
def isOdd (n):
	
	return n%2 != 0

def odd(n):
	
	return 3*n + 1

def even(n):
	
	return n/2
	
def collatz(n):
	
	if(n==1):
		return n
	
	if isOdd(n):
		return odd(n)
	else:
		return even(n)

a = 0

b = 0

t = 0

# 3 -> 
while (t < 20):
	n_input = t+1
	count = 1
	while 1:
		count += 1
		n_input = collatz(n_input)
		print n_input, 
		if n_input == 1:
			print 'count', count
			print 'a', a
			a = max(count,a)
			print 'max', a
			break
	t += 1
