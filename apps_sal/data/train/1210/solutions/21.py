t = int(input())
while t:
    (n, p) = map(int, input().split())
    (s, l) = map(str, input().split())
    p_l = p
    p_r = n - p + 1
    l1 = 'H'
    if l == 'H':
        l1 = 'E'
    if s == 'L':
        if p_l % 2 == 1:
            print(f'{p_l} {l}')
        else:
            print(f'{p_l} {l1}')
            print()
    elif p_r % 2 == 1:
        print(f'{p_r} {l}')
    else:
        print(f'{p_r} {l1}')
    t -= 1
