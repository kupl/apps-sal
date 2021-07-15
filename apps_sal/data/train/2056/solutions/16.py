N = int(input())
A = input()
B = input()
ans = 0
n = 0
while n < N:
	if A[n] != B[n]:
		ans += 1
		if n+1<N and A[n+1]==B[n] and B[n+1]==A[n]:
			n += 2
		else:
			n += 1
	else:
		n += 1
print(ans)

