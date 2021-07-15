# def makelist(n, m):
# 	return [[0 for i in range(m)] for j in range(n)]

# n = int(input())
# a, b = map(int, input().split())
# s = input()


N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

diff = [0]*N

mini = A[0]
for i in range(1, N):
	now = A[i]
	if now <= mini:
		mini = now
	else:
		diff[i] = now - mini

sa = max(diff)

ans = 0
mini = A[0]
l = 1
r = 0
for i in range(1, N):
	now = A[i]
	if mini == now:
		l += 1
	elif now < mini:
		if r > 0:
			ans += min(l, r)
			r = 0
		mini = now
		l = 1
	else: # now > mini
		if now - mini == sa:
			r += 1

if r > 0:
	ans += min(l, r)
print(ans)

