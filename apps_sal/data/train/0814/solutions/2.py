def isOne(slen):
    count = 0
    for i in slen:
        if(i == 1):
            count += 1
        else:
            return False
    return count == 1


def isOdd(slen):
    for i in slen:
        if(i % 2 == 1 and i > 1):
            return True
    else:
        return False


T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]

    slen = []
    i = 0
    while(i < N):
        if(A[i] == 0):
            e = i
            while(e < N and A[e] == 0):
                e += 1
            slen.append(e - i)
            i = e + 1
        else:
            i += 1

    if(len(slen) != 0 and (isOne(slen) or isOdd(slen))):
        ans.append('Yes')
    else:
        ans.append('No')

for i in ans:
    print(i)
