import bisect
N = int(input())
a = list(map(int, input().split()))
big_list = []
num_list = []
biggest = 0
for (i, a_i) in enumerate(a):
    if a_i > biggest:
        big_list.append(a_i)
        num_list.append(i)
        biggest = a_i
big_list.append(10 ** 10)
big_list.append(0)
num_list.append(0)
num_list.append(0)
ans = [0] * N
a.sort()
j = 0
for (i, a_i) in enumerate(a):
    if a_i < big_list[j]:
        ans[num_list[j]] += a_i - big_list[j - 1]
    else:
        ans[num_list[j]] += (big_list[j] - big_list[j - 1]) * (N - i)
        j += 1
for i in range(N):
    print(ans[i])
