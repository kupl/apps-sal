import sys

n = int(input())

v = [ list(map(int, input().split())) for i in range(n)]

res = []

for i in range(n):
	if v[i][2] >= 0:
		res.append(i + 1)
		dec = 0
		for j in range(i + 1, n):
			if v[j][2] >= 0:
				if v[i][0] > 0:
					v[j][2] -= v[i][0]
					v[i][0] -= 1
				v[j][2] -= dec
				if v[j][2] < 0: dec += v[j][1]

print(len(res))
print(" ".join(map(str, res)))
