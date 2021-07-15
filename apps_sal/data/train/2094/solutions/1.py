n = int(input())
s = input()
ones = 0
for i in s:
	if i == 'n':
		ones += 1
for i in range(ones):
	print(1, end = " ")
for j in range((n-ones*3)//4):
	print(0, end = " ")
