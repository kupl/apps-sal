for _ in range(int(input())):
    n = int(input())
    s = input()
    aa = ['A', 'E', 'I', 'O', 'U']
    a = 0
    if 'A' in s:
        a += s.count('A')
    if 'E' in s:
        a += s.count('E')
    if 'I' in s:
        a += s.count('I')
    if 'O' in s:
        a += s.count('O')
    if 'U' in s:
        a += s.count('U')
    kk = 0
    if a > 1:
        for i in range(n - 1):
            if s[i] in aa and s[i + 1] in aa:
                print('Yes')
                kk = 1
                break
        if kk == 0 and s[0] in aa and (s[n - 1] in aa):
            print('Yes')
            kk = 1
    else:
        kk = 1
        print('No')
    if kk == 0:
        print('No')
