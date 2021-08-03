s = input().split()
k = min(s, key=len)
n = len(s)
print(k, end=" ")
for i in range(n):
    print(s[i], k, end=" ")
