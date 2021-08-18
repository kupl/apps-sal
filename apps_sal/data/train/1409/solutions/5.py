import sys
T = int(input())
for t in range(T):
    N = int(sys.stdin.readline().strip())
    cnt = 0
    while(N != 0):
        N = N & (N - 1)
        cnt += 1
    print(cnt)
