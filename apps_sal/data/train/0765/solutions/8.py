n = int(input())
L = list(map(int, input().split()))
q = int(input())
F = [0 for i in range(100055)]
i = 1
for t in L:
    F[i] = t
    i += 1
while q > 0:
    q -= 1
    l1 = list(map(int, input().split()))
    if l1[0] == 1:
        F[l1[1]] = l1[2]
    else:
        r = l1[1]
        enjoy = F[1]
        k = 1
        while 1:
            if 1 + k * r > n:
                break
            enjoy = enjoy * F[1 + k * r]
            k += 1
        temp = enjoy
        while 1:
            if temp // 10 == 0:
                print(temp, end=' ')
                break
            temp = temp // 10
        print(enjoy % 1000000007)
