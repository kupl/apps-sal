q = int(input())
for rwwe in range(q):
	n = int(input())
	spent = 0
	while n >= 10:
		x = (n-(n%10))
		spent += x
		n -= x
		n += x//10
	spent += n
	print(spent)
