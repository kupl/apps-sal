n = list(map(int, input().split()))[0]
lst = list(map(int, input().split()))
sorted_index = sorted(range(n), key=lambda k: lst[k], reverse=True)
lookup = [(0, 0)] * n
res = []
res_pos = 1
for index in sorted_index:
    seq_len = lookup[index][0] + lookup[index][1] + 1
    if seq_len >= res_pos:
        step = seq_len - res_pos + 1
        res += [lst[index]] * step
        res_pos += step
    step_back = lookup[index][0] + 1
    if index - step_back >= 0:
        lookup[index - step_back] = (lookup[index - step_back][0], lookup[index - step_back][1] + 1 + lookup[index][1])
    step_forward = lookup[index][1] + 1
    if index + step_forward < n:
        lookup[index + step_forward] = (lookup[index + step_forward][0] + 1 + lookup[index][0], lookup[index + step_forward][1])
res = list(map(str, res))
print(' '.join(res))
