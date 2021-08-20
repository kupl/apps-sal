T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    guest = 0
    for i in range(N):
        if A[i] <= guest:
            guest += 1
    ans.append(guest)
for i in ans:
    print(i)
