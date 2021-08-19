for _ in range(int(input())):
    (n, m, s) = [int(x) for x in input().split()]
    h = list(map(int, input().split()))
    h.sort()
    sum = 0
    count = 0
    for i in h:
        if i <= s and m > 0:
            m -= 1
            count += 1
        elif i <= s * 2 and m > 1:
            m -= 2
            count += 1
        if m == 0:
            break
    print(count)
