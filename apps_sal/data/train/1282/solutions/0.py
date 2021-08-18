l = []
for i in range(62):
    l.append(2**i)
T = int(input())

flag = 0
for t in range(T):
    L, R = [int(i) for i in input().split()]
    bL = bin(L)
    lL = len(bL) - 2
    index = 1
    ans = 0
    temp = 0

    while(index <= lL):
        temp = L % l[index]
        if temp >= l[index - 1]:
            if(l[index] - temp <= R - L + 1):
                ans = (ans + (l[index - 1]) * (l[index] - temp)) % 1000000007
            else:
                ans = (ans + (l[index - 1]) * (R - L + 1)) % 1000000007

        index += 1
    print(ans)
