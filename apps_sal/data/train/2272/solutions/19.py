from bisect import bisect_left, bisect_right
N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

num = [0] * 30
for i in range(30):
    t = pow(2, i)
    K = sorted(i % (2 * t) for i in A)
    L = sorted(i % (2 * t) for i in B)
    # L=sort()
    # print(K,L)
    a = 0
    # 尺取り法,i*tより小さい整数を数える
    S = [i * t for i in range(1, 5)]
    count = [N] * 4
    for k in K:
        for j in range(4):
            while L[count[j] - 1] + k >= S[j] and count[j] > 0:
                count[j] -= 1
        a += count[3] - count[2] + count[1] - count[0]
        # print(count,a)
    num[i] = a % 2
ans = 0
s = 1
for z in num:
    ans += z * s
    s *= 2
print(ans)
