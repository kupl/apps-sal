import fractions, functools
n = int(input())
a = list(map(int, input().split()))
gcd = functools.reduce(fractions.gcd, a)
moves = max(a) // gcd - n
print(['Bob', 'Alice'][moves % 2])

