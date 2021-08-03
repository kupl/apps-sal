for _ in range(int(input())):
    a = list(input())
    n = len(a)
    for i in reversed(range(n)):
        if a[i] == '1':
            a.pop()
        else:
            break
    n = len(a)
    zero = 0
    prev = tot = 0
    c = 0
    for i in reversed(range(n)):
        if a[i] == '0':
            zero += 1
            continue
        if prev != zero:
            prev = zero
            c += 1
        tot += c + zero
    print(tot)
