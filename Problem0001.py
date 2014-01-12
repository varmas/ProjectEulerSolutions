def gcd(a, b):
	while b != 0:
		t = b
		b = a % b
		a = t
		
	return a

def a_sum(a,n):
	n-=1
	_n = 1
	sum = 0
	while _n <= (n)/a:
		sum += _n*a
		_n += 1
		
	return sum

def a35a(a,b,n):
	a_b = a*b/gcd(a,b)
	sum = a_sum(a,n) + a_sum(b,n) - a_sum(a_b,n)
	
	return sum

# 3
a = input()
# 5
b = input()
# 1000
n = input()

print a35a(a, b, n)	
