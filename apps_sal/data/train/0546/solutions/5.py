try:
    t = int(input())
    for _ in range(t):
        N = int(input())
        a = bin(N)
        print(a.count('1') - 1)
except:
    pass
