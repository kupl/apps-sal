T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    ans = "NO"
    a_s,bs,cs = A*A,B*B,C*C
    if (a_s==bs+cs or bs==a_s+cs or cs==a_s+bs) and A>0 and B>0 and C>0:
        ans = "YES"
    print(ans)
