n = int(input())
f = [int(x) for x in input().split()]
q = int(input())
while q != 0:
    q = q - 1
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        f[query[1] - 1] = query[2]
        continue
    elif query[0] == 2:
        ans = f[0]
        if ans == 0:
            print('0 0')
            continue
        i = 1
        r = query[1]
        while i * r < n:
            ans = ans * f[i * r]
            i += 1
        print(str(ans)[0], ans % 1000000000)
