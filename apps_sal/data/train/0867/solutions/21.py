for _ in range(int(input())):
    (s, a, b, c) = list(map(int, input().split()))
    l = []
    l.extend([c, b, a])
    c = 0
    sum = 0
    for i in range(3):
        x = l.pop()
        sum += x
        if sum < s:
            pass
        elif sum == s:
            c += 1
            sum = 0
        else:
            c += 1
            sum = x
    if sum < s and sum != 0:
        c += 1
    print(c)
