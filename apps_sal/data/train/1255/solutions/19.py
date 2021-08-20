t = int(input())
while t > 0:
    (s, k) = input().split()
    s = list(s)
    k = int(k)
    anstr = ''
    for i in range(97, 123):
        if chr(i) in s:
            if k > 0:
                anstr = anstr + chr(i)
                k = k - 1
        else:
            anstr = anstr + chr(i)
    if len(anstr) >= len(s):
        print(anstr[:len(s)])
    else:
        print('NOPE')
    t = t - 1
