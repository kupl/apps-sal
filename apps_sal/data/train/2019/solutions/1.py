n = int(input())
A = list(map(int, input().split()))

ans = (sum(A) + (n - 2)) // (n - 1)
if (ans < max(A)):
    ans = max(A)
print(ans)
