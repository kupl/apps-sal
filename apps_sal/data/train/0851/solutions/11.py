ans = ""
for t in range(int(input())):
	n, k = map(float, input().split())
	ans += str(2*(n - (n-1)/k)) + "\n"

print(ans)
