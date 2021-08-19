a = ['AA', 'AE', 'AI', 'AO', 'AU', 'EA', 'EE', 'EI', 'EO', 'EU', 'IA', 'IE', 'IO', 'II', 'IU', 'OA', 'OE', 'OI', 'OO', 'OU', 'UA', 'UE', 'UI', 'UO', 'UU']
for i in range(int(input())):
    n = int(input())
    s = input()
    b = 0
    for m in a:
        if m in s:
            b = 1
            break
    p = []
    p.append(s[0])
    p.append(s[n - 1])
    p = ''.join(p)
    if n <= 3:
        print('No')
    elif b == 0 and p not in a:
        print('No')
    else:
        print('Yes')
