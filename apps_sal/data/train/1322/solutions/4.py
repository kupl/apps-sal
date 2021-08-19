for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = [int(x) for x in input().split()]
    s.sort(reverse=True)
    count = 0
    req = s[k - 1]
    for x in s:
        if x >= req:
            count += 1
        else:
            break
    print(count)
