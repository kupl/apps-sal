test = int(input())
for _ in range(test):
    n = int(input())
    n = list(bin(n))
    ans = n.count('1')
    print(ans - 1)
