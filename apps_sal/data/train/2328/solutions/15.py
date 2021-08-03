# cook your code here
a = []
b = []
c = []
temp = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def find(temp, f):
    q = -1
    while q < len(temp) - 1 and temp[q + 1] <= f:
        q = q + 1
    if q == -1:
        return 0
    if temp[q] == f:
        return 1
    else:
        f = f - temp[q]
        flag = find(temp[0:q], f)
        return flag


for i in range(0, a[1]):
    c = list(map(int, input().split()))
    if c[0] == 3:
        temp = b[c[1] - 1:c[2]]
        temp.sort()
        # print temp
        j = -1
        f = int(c[3])

        while j < len(temp) - 1 and temp[j + 1] <= f:
            j = j + 1

        if temp[j] == f:
            print('Yes')
            continue

        while j >= 1:

            f = c[3] - temp[j]

            flag = find(temp[0:j], f)

            if flag == 1:
                break
            else:
                j = j - 1

        if flag == 1:
            print('Yes')
        else:
            print('No')

    if c[0] == 1:
        b[c[1] - 1] = c[2]
    if c[0] == 2:
        b[c[1] - 1:c[2]] = reversed(b[c[1] - 1:c[2]])
