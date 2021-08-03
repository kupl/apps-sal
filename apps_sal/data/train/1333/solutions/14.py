M = 1000000007
T = int(input())
for _ in range(T):
    n = int(input())
    l = [int(i) for i in input().split()]
    count1 = 0
    for i in range(1, n):
        if((l[i - 1] & l[i]) != l[i - 1]):
            count1 = 0
            break
        else:
            count1 += (bin(l[i - 1] & l[i]).count("1"))

    if(count1 == 0):
        print(count1)
    else:
        print((2**count1) % M)
