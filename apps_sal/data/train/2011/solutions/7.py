n = int(input())
ans = [i for i in range(max(0, n - 100), n) if i + sum((int(j) for j in str(i))) == n]
print(len(ans), '\n' + '\n'.join(map(str, ans)))
