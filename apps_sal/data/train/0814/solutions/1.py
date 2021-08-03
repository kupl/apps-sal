def isOdd(slen):
    m = -float('inf')
    mi = None
    for i in range(len(slen)):
        if(slen[i] % 2 == 1 and slen[i] > m):
            mi = i
            m = slen[i]
    return mi


def find_even(slen, mi):
    for i in range(len(slen)):
        if(i != mi and slen[i] > slen[mi] // 2):
            return False
    return True


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

    x = isOdd(slen)
    if(len(slen) != 0 and x != None and find_even(slen, x)):
        ans.append('Yes')
    else:
        ans.append('No')

for i in ans:
    print(i)
