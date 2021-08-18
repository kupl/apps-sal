def answer():
    for t in range(int(input())):
        N, K = [int(x) for x in input().split()]
        l = [-1]
        l += [int(x) for x in input().split()]
        green = 0
        orange = 0
        red = 0
        ans = 0

        while True:
            orange += 1

            if orange == N + 1:
                ans = max(ans, N - green)
                break

            elif l[orange] > K:

                red = orange
                while True:
                    red += 1
                    if red == N + 1:
                        ans = max(ans, N - green)
                        break
                    elif l[red] > K:
                        if l[red] != l[orange]:
                            ans = max(ans, red - green - 1)
                            green = orange
                            orange = red - 1
                            break
                        else:
                            orange = red

        print(ans)
    return


def __starting_point():

    answer()


__starting_point()
