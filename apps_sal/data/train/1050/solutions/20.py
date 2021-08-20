T = int(input())
while T:
    check = []
    s = input()
    cur = 0
    long_prifix = 0
    for i in s:
        cur += 1
        if i == '<':
            check.append(i)
        elif i == '>' and len(check):
            check.pop()
            if not check:
                long_prifix = cur
        else:
            break
    print(long_prifix)
    T -= 1
