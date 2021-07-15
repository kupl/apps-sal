def evens(A):
    n = len(A)
    l = n//2-1; r = n//2
    if len(A)%2 == 1: l+= 1
    ans = [max(A[l], A[r])]
    while r < n-1:
        l-= 1; r+= 1
        ans.append(max(ans[-1], A[l], A[r]))
    return ans

def interleave(A, B):
    q = []
    for i in range(len(B)): q+= [A[i], B[i]]
    if len(A) != len(B): q.append(A[-1])
    return q

n = int(input())
A = list(map(int,input().split()))
M = [min(A[i],A[i+1]) for i in range(n-1)]
ansA = evens(A)
ansM = evens(M) if n>1 else []
if n%2 == 0: print(*interleave(ansA, ansM[1:]), max(A))
else: print(*interleave(ansM, ansA[1:]), max(A))
