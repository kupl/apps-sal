for i in range(int(input())):
    n = int(input())
    b = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]
    boy = sorted(b)
    girl = sorted(g)
    f = 0
    for k in range(n - 1):

        if girl[k] < boy[k]:
            if girl[k + 1] < boy[k]:
                f = 1
                break

        elif girl[k] > boy[k]:

            if girl[k] > boy[k + 1]:
                f = 1
                break
    if girl[0] < boy[0]:
        if girl[n - 1] > boy[n - 1]:
            f = 1
    elif boy[0] < girl[0]:
        if boy[n - 1] > girl[n - 1]:
            f = 1

    if f == 1:
        print("NO")
    else:
        print("YES")
