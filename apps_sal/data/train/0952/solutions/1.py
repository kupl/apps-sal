t = int(input())
while t > 0:
    s = input()
    a = [1, 5, 9, 15, 21]
    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    k = []
    for i in range(len(s)):
        for j in range(len(b)):
            if s[i] == b[j]:
                k.append(j + 1)
                break
    c = []
    for i in range(len(k)):
        min = 10000
        for j in range(len(a)):
            p = abs(k[i] - a[j])
            if p <= min:
                min = p
        c.append(min)
    s = 0
    for i in range(len(c)):
        s = s + c[i]
    print(s)
    t -= 1
