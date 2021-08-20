T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    if N <= 2:
        print('YES')
    else:
        unique_c = {}
        for c in S:
            if c in list(unique_c.keys()):
                unique_c[c] += 1
            else:
                unique_c[c] = 1
        safe = 0
        no_odd = 0
        for c in list(unique_c.keys()):
            if unique_c[c] % 2 != 0:
                no_odd += 1
        if N // 2 % 2 == 1:
            if no_odd == 2 or no_odd == 0:
                print('YES')
            else:
                print('NO')
        elif no_odd != 0:
            print('NO')
        else:
            print('YES')
