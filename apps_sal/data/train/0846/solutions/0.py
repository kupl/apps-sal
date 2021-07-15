K,A,B = map(int,input().split())
 
if A + 2 > B:
    print(K + 1)
    return
 
start = A - 1
K -= start
ans = K//2 * (B-A) + K%2 + start + 1
print(ans)
