for _ in range(int(input())):
    n, u, d = list(map(int, input().split()))
    hills = list(map(int, input().split()))
    u *= -1

    curr = hills[0]
    count = 0
    para = True
    for h in hills[1:]:
        if u <= curr - h <= d:
            count += 1
        elif para and curr - h > 1:
            count += 1
            para = False
        else:
            break

        curr = h

    print(count + 1)
