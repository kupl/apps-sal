t = int(input())
for _ in range(t):
    (s, k) = input().split()
    k = int(k)
    n = len(s)
    x = list(set(s))
    final = ''
    for i in range(97, 123):
        if chr(i) in x:
            if k > 0:
                final += chr(i)
                k -= 1
            else:
                continue
        else:
            final += chr(i)
    if len(s) <= len(final):
        print(final[:n])
    else:
        print('NOPE')
