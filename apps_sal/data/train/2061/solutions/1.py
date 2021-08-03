
for _ in range(int(input())):
    Z = list(map(int, input().split()))
    X = sum(Z[::2])
    Y = sum(Z[1::2])

    if sum(Z[:4]) % 2 == 0:
        X += Z[4]
        Y += Z[5]

    elif sum(Z[2:]) % 2 == 0:
        X += Z[0]
        Y += Z[1]

    else:
        X += Z[2]
        Y += Z[3]

    if X != Y:
        print((max(abs((X - 1) // 2), abs((Y - 1) // 2))))

    else:

        if X == 1 and Y == 1:
            print((0))

        elif X == 3 and Y == 3:
            print((1))

        else:
            print((max(abs((X - 1) // 2), abs((Y - 1) // 2)) + 1))
