def subset(n, s, l):
    t = 1 << n
    for i in range(1, t):
        temp = 0
        for j in range(n):
            if i & 1 << j:
                temp += l[j]
        if temp == s:
            return True
    return False


for _ in range(int(input())):
    l = list(map(int, input().split()))
    print('Yes' if subset(len(l), 0, l) else 'No')
