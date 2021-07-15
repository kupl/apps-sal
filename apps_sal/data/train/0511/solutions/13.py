n = int(input())
a_ls = list(map(int, input().split()))
s_ls = [0] * n
Sum = 0
for i in range(n):
    Sum = Sum ^ a_ls[i]
for i in range(n):
    s_ls[i] = Sum ^ a_ls[i]
print(*s_ls)
