try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = input()
        i, res = 0, 0
        while(i < n):
            count = 0
            while(i < n - 1 and l[i] == l[i + 1]):
                i += 1
                count += 1
            res += count
            i += 1
        print(res)
except EOFError:
    pass
