t = int(input())
for t in range(t):
    (n, k) = list(map(int, input().split()))
    s = input()
    i = 0
    j = 0
    a = 0
    while i < n and j < n:
        if s[i] == 'M':
            if s[j] == 'I':
                c = 0
                if i > j:
                    z = s[j:i]
                    c = z.count(':')
                else:
                    z = s[i:j]
                    c = z.count(':')
                p = k + 1 - abs(i - j) - c
                if p > 0:
                    a += 1
                    i += 1
                    j += 1
                elif i < j:
                    i += 1
                else:
                    j += 1
            elif s[j] == 'X':
                j += 1
                i = j
            else:
                j += 1
        elif s[i] == 'X':
            i += 1
            j = i
        else:
            i += 1
    print(a)
