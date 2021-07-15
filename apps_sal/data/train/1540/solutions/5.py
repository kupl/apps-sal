T = int(input())
for i in range(T):
    N = int(input())
    K = int(input())
    if K%N == 0 and K >= N:
        print('YES')
    else:
        print("NO")
