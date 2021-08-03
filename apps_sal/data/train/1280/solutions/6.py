t = int(input())
for _ in range(t):
    a = input().strip()
    a = list(a)
    b = 'abcdefghijklmnopqrstuvwxyz'
    if a == a[::-1]:
        print(0)
    else:
        c = 0
        j = len(a) - 1
        for i in range(0, len(a) // 2):
            if a[i] != a[j]:
                k = max(a[i], a[j])
                p = min(a[i], a[j])
                c += ord(k) - ord(p)
            j -= 1
        print(c)
