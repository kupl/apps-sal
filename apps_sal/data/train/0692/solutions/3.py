n = eval(input())
a = list(map(int, input().split()))
q = eval(input())
while q:
    s = input().split()
    if s[0] == 'U':
        l = int(s[1])
        v = int(s[2])
        a[l - 1] = v
    if s[0] == 'A':
        l = int(s[1])
        r = int(s[2])
        print(sum(a[l - 1:r]))
    if s[0] == 'M':
        l = int(s[1])
        r = int(s[2])
        print(max(a[l - 1:r]))
    if s[0] == 'm':
        l = int(s[1])
        r = int(s[2])
        print(min(a[l - 1:r]))
    if s[0] == 'S':
        l = int(s[1])
        r = int(s[2])
        A = sorted(a[l - 1:r], reverse=True)
        print(A[1])
    if s[0] == 's':
        l = int(s[1])
        r = int(s[2])
        A = sorted(a[l - 1:r])
        print(A[1])
    q -= 1
