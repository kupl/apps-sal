def sum_digits(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans


n = int(input())
ans = []
for i in range(max(1, n - 1000), n + 1):
    if (i + sum_digits(i) == n):
        ans.append(i)
print(len(ans))
for elem in ans:
    print(elem)
