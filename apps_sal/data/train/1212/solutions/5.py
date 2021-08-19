for i in range(int(input())):
    s = input()
    l = [0 for i in range(26)]
    for i in s:
        l[ord(i) - 65] += 1
    l.sort()
    n = len(s)
    ans = float('inf')
    for i in range(1, 27):
        temp = 0
        if n % i == 0:
            p = n // i
            for j in range(26 - i):
                temp += l[j]
            for j in range(26 - i, 26):
                if l[j] > p:
                    temp += l[j] - p
            ans = min(ans, temp)
    print(ans)
