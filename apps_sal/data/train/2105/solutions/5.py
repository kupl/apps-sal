
def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

n = int(input())

colors = []

for i in range(2, n + 2):
	if not is_prime(i):
		colors.append(str(2))
	else:
		colors.append(str(1))
		
if n >= 3:
	print(2)
else:
	print(1)

print(" ".join(colors))
