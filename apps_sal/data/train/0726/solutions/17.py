for _ in range(int(input())):
    n = int(input())
    a = []
    d = [0] * (26)
    for i in range(n):
        for k in input():
            d[ord(k) - ord('a')] += 1
    a.append(d[2] // 2)
    a.append(d[14])
    a.append(d[3])
    a.append(d[4] // 2)
    a.append(d[7])
    a.append(d[5])
    print(min(a))
