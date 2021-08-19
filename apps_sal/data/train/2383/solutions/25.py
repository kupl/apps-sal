T = int(input())
for t in range(T):
    (A, B) = list(map(int, input().split()))
    mini = min([A, B])
    maxi = max([A, B])
    res = max(2 * mini, maxi)
    print(res * res)
