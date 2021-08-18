try:
    for _ in range(int(input())):
        N, K = map(int, input().split())
        memory = list(map(int, input().split()))
        memory.sort()
        a = memory[:K]
        b = memory[K:]
        memory.reverse()
        c = memory[:K]
        d = memory[K:]
        a = sum(a)
        b = sum(b)
        c = sum(c)
        d = sum(d)
        print(max(abs(a - b), abs(c - d)))
except:
    pass
