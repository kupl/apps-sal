def check(z, i, j, r):
    x = j - i
    if r[z][i] == r[z][j] == r[z + x][i] == r[z + x][j]:
        return True
    return False


t = int(input())
while(t):
    t -= 1
    count = 0
    a = list((map(int, input().split())))
    r = []
    for h in range(a[0]):
        p = list(input())
        r.append(p)
    # print(r)
    for z in range(a[0]):
        for i in range(a[1]):
            for j in range(i + 1, a[1]):
                x = j - i
                if x <= (a[0] - z - 1):
                    if check(z, i, j, r) == True:
                        count += 1
                else:
                    break
    print(count)
