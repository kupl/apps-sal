for _ in range(int(input())):
    s, n = list(map(int, input().split()))
    count = 0
    if s > n:
        rem = s % n
        count += (s // n)
        if rem % 2 == 0:
            if rem != 0:

                count += 1
        else:
            if rem == 1:
                count += 1
            else:
                count += 2
    elif s < n:
        if s % 2 == 0:
            count += 1
        else:
            if s == 1:
                count += 1
            else:
                count += 2
    else:
        count += 1

    print(count)
