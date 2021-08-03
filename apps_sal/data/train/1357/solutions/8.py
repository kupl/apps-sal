
for _ in range(int(input())):
    has = 1
    get = []
    tens = 0
    flag = 1
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N):
        get.append(a[i] - 5)

    if a[0] != 5 or a[1] == 15:
        flag = 0

    else:
        for i in range(1, N):
            if get[i] == 0:
                has = has + 1

            elif get[i] == 5:

                # if tens!=0:
                #                        has=has-10
                #                        tens=tens-1
                if has >= 1:
                    has = has - 1
                else:
                    flag = 0
                    break
                tens = tens + 1
            else:
                if tens != 0:
                    tens = tens - 1
                elif has >= 2:
                    has = has - 2

                else:
                    flag = 0
                    break

    if flag == 0:
        print("NO")

    else:
        print("YES")
