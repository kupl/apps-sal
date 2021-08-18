try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        sum, c = 0, 0
        for i in range(len(l)):
            for j in range(i, len(l) - 1):
                sum = sum + l[j] + l[j + 1]
                if sum % 2 != 0:
                    c = c + 1
        print(c)
except:
    pass
