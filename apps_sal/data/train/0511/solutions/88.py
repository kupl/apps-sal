from functools import reduce
N = int(input())
A = list(map(int, input().split()))
m = reduce(lambda a, b: a^b, A)
l = list(map(str, [a ^ m for a in A]))
ans = ' '.join(l)
print(ans)
