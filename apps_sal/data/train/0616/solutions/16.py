for _ in range(int(input())):

    r, c = map(int, input().split())

    ans = 0

    last = -1
    flag = 0

    for i in range(r):

        j = 0

        values = []

        for car in input().split():

            if(car == "P"):
                values.append(j)

            j += 1

        if(len(values) == 0):
            if(flag == 0):
                continue
            else:
                ans += 1
                continue

        flag = 1

        if(i % 2 == 1):

            ans += abs(min(values) - max(values)) + 1

            if(i == r - 1):
                ans -= 1

            if(last == -1):
                last = min(values)
            else:

                ans += abs(last - max(values))

            last = min(values)

        else:

            ans += abs(max(values) - min(values)) + 1

            if(i == r - 1):
                ans -= 1

            if(last == -1):
                last = max(values)
            else:
                ans += abs(last - min(values))

            last = max(values)

    print(ans)
