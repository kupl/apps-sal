T = int(input())


def bSearch(A, suff, k, i, j):
    if i >= len(A):
        return
    if i == j:
        if suff[i] == False or A[j] <= A[k]:
            return
        return i
    mid = (i + j) // 2
    if mid <= k:
        return bSearch(A, suff, k, mid + 1, j)
    elif A[mid] <= A[k] or suff[mid] == False:
        return bSearch(A, suff, k, mid + 1, j)
    else:
        return bSearch(A, suff, k, i, mid)


for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    pref = [False for _ in range(N)]
    suff = [False for _ in range(N)]
    pref[0] = True
    suff[-1] = True
    for i in range(1, N):
        if A[i] > A[i - 1]:
            pref[i] = True
        else:
            break
    for i in reversed(range(N - 1)):
        if A[i] < A[i + 1]:
            suff[i] = True
        else:
            break
    count = 0
    for i in range(N):
        if pref[i] == True:
            j = bSearch(A, suff, i, i + 1, N - 1)
            if j == None:
                if i < N - 1:
                    count += 1
            elif j == i + 1:
                count += N - j
            else:
                count += N - j + 1
    for i in range(1, N):
        if suff[i] == True:
            count += 1
    print(count)
