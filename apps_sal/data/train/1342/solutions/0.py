import math
for i in range(int(input())):
    n, x = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l.sort()
    flag = 0
    d = 0

    for j in range(n):

        if l[j] > x:
            for k in range(j, n):

                if x < l[k]:

                    d += (math.ceil(math.log(l[k] / x) / math.log(2)) + 1)

                else:
                    d += 1

                x = l[k] * 2

                flag = 1

            break

    if flag == 1:

        print(j + d)
    else:
        print(n)
