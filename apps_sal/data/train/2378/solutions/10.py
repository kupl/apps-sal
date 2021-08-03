for _ in range(int(input())):
    s = input()
    l, r, d, u = s.count('L'), s.count('R'), s.count('D'), s.count('U')
    if max(min(d, u), min(l, r)) == 0:
        print(0)
        print()
        continue
    if min(d, u) == 0:
        print(2)
        print('LR')
        continue
    if min(l, r) == 0:
        print(2)
        print('DU')
        continue

    ans = 'L' * min(l, r) + 'D' * min(u, d) + 'R' * min(l, r) + 'U' * min(u, d)
    print(len(ans))
    print(ans)
