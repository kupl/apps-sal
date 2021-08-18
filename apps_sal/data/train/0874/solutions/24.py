for _ in range(int(input())):
    n, m, s = list(map(int, input().split()))
    arr = [int(a) for a in input().split()]
    count = 0
    arr.sort()
    for x in arr:
        if x <= s and m > 0:
            m -= 1
            count += 1
        elif x <= 2 * s and m > 1:
            m -= 2
            count += 1
    print(count)
