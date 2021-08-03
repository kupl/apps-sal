import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
flag = [1] * n
r = n - 1
cnt = 0

print(1, end=' ')

for i in range(n - 1):
    flag[p[i] - 1] = 0

    while flag[r] == 0:
        r -= 1
        cnt += 1

    print(i + 2 - cnt, end=' ')

print(1)
