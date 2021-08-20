t = int(input())
while t > 0:
    t -= 1
    (s, k) = input().split()
    k = int(k)
    n = len(s)
    d = []
    for i in range(97, 97 + 26):
        d.append(chr(i))
    st = ''
    for i in d:
        if i not in s:
            st += i
        elif k > 0:
            st += i
            k -= 1
        if len(st) == n:
            print(st)
            break
    if len(st) < n:
        print('NOPE')
