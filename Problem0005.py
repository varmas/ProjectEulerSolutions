# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(a, b):
	while b != 0:
		t = b
		b = a % b
		a = t
		
	return a

def lcm(a,b):
	return a*b/gcd(a,b)

n = 2	

limit = 20

lcm_value = 1

while(n<=limit):
	lcm_value = lcm(lcm_value,n)
	n+=1
	
print lcm_value
