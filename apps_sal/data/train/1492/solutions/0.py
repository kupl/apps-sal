t = int(input())
for j in range(0, t):
    n = int(input())
    m = 100
    for i in range(0, n):
        str = input()
        p = min(str.count("a", 0, len(str)), str.count("b", 0, len(str)))
        if (m > p):
            m = p
    print(m)
    t = t - 1
