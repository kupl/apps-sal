def summ(x):
    return sum([int(i) for i in str(x)])

n = int(input())
ans = []
for i in range(max(1, n - 200), n):
    if i + summ(i) == n:
        ans.append(i)
print(len(ans))
print(*ans)
