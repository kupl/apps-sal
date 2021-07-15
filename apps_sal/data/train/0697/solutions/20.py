from sys import stdin, stdout
input = stdin.readline
print2 = stdout.write
def get_ints(): return map(int, stdin.readline().split())
def get_list(): return list(map(int, stdin.readline().split()))
for _ in range(int(input())):
	n, k = get_ints()
	powers = get_list()
	s = sum(powers[0:k])
	ma = s
	i = 1
	while i + k - 1 < n:
		s = s - powers[i-1] + powers[i+k-1]
		ma = max(s, ma)
		i += 1
	print(ma)
