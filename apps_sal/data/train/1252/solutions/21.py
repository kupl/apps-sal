try:

    def findprimes(n, l):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        for i in range(2, n + 1):
            if prime[i] == True:
                l.append(i)
        return l
    for _ in range(int(input())):
        n = int(input())
        l = []
        findprimes(n, l)
        s = sum(l)
        print(s % 10)
except:
    pass
