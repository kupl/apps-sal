# cook your dish here
def ConDecBin(num, count):
	count += num%2
	if num > 1:
		ConDecBin(num//2, count)
	else:
		print(count - 1)

for k in range(int(input())):
	num = int(input())
	count = 0

	ConDecBin(num, count)
