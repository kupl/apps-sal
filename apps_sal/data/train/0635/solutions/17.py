n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
M = 10**9 + 7
farr = []
j = 0
f = 0
c = 0
while(j < len(l)):
    if f == 0:
        f = l[j]
        c = c + 1
        if j == len(l) - 1:
            farr.append(c)

        j = j + 1

    elif(f != 0):
        if l[j] == f:
            c = c + 1
            if j == len(l) - 1:
                farr.append(c)

            j = j + 1

        else:
            farr.append(c)
            f = 0
            c = 0

cnt = 1
arr = farr.copy()
z = 1
while(z <= k):
    if z == 1:
        cnt = cnt + len(l) % M

    else:
        ic = 0
        i = 0
        kc = 0
        while(i < len(farr)):
            kc = arr[i]
            arr[i] = (ic * farr[i]) % M
            ic = ic + kc
            cnt = (cnt + arr[i]) % M
            i = i + 1

    z = z + 1

print(cnt % M)
