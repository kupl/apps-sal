N = int(input())
A = [0] + list(map(int, input().split()))
B = [[a, i, 1] for i, a in enumerate(A)]
C = sorted(B, reverse=True)
a_max, idx = 0, 0  # [value, idx]
left_max = [[0, 0] for i in range(N + 1)]  # [value, idx]
for i, a in enumerate(A):
    left_max[i] = [a_max, idx]
    if a > a_max:
        a_max, idx = a, i

ans = [0] * (N + 1)
next_i = C[0][1]
for _, i, _ in C:
    a, _, num = B[i]
    if i == next_i:
        next_a, next_i = left_max[i]
        now_i = i
        ans[i] += (a - next_a) * num
        B[next_i][2] += num
    else:
        ans[now_i] += (a - next_a) * num
        B[next_i][2] += num

print(*ans[1:], sep='\n')
