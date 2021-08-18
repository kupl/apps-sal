import copy

N = int(input())
A = list(map(int, input().split()))
B = copy.copy(A)
B.sort()

place_dict = {0: 0}
num_list = []
ct_dict = {}
i = 1
for b in B:
    if b not in place_dict:
        place_dict[b] = i
        num_list.append(b)
        ct_dict[b] = 1
        i += 1
    else:
        ct_dict[b] += 1

tmp = 0
tasks = [(0, 0)]
i = 0
for a in A:
    i += 1
    if tmp < a:
        tmp = a
        tasks.append((a, i))

M = len(num_list)
ans = [0 for _ in range(N)]
j = M - 1
ct_abv = 0
for i in range(len(tasks) - 1, 0, -1):
    tmp = 0
    nxt = tasks[i - 1][0]
    while num_list[j] > nxt and j >= 0:
        ct_abv += ct_dict[num_list[j]]
        if j == 0:
            tmp += ct_abv * num_list[0]
        else:
            tmp += ct_abv * (num_list[j] - num_list[j - 1])
        j -= 1
    ans[tasks[i][1] - 1] = tmp

print(*ans, sep="\n")
