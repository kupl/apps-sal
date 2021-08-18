t = int(input())
for _ in range(t):
    p = input()

    cnt, maxi, ans = 1, 1, 0

    for i in p:

        if i == '
           if cnt > maxi:
                maxi = cnt
                ans += 1

            cnt = 1

        elif i == '.':
            cnt += 1

        elif i == '
           continue

    if cnt != 1:
        if cnt > maxi:
            ans += 1

    print(ans)
