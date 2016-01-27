'''
Url: https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

f = [1,2]
total = 2

while sum(f) < 4000000:
	nextitem = sum(f)
	if nextitem % 2 == 0:
		total += nextitem
	f = [f[1], nextitem]

print total # 4613732
