t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    l = list(map(str, input().split()))
    i = n - 1
    for j in range(k):
        if l[i] == 'T':
            l.pop(i)
            i = i - 1
        else:
            l.pop(i)
            i = i - 1
            for k in range(len(l)):
                if l[k] == 'H':
                    l[k] = 'T'
                else:
                    l[k] = 'H'
    print(l.count('H'))
