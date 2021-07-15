n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ans = [1] * n
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if(a[j] % a[i] == 0):
            ans[i] = max(ans[i], 1 + ans[j])
print(max(ans))
