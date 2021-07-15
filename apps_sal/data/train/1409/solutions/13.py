cases = int(input())
for _ in range(cases):
    a = int(input())
    a = bin(a)
    c = a.count('1')
    print(c)
