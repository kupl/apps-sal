n = int(input())
d = [int(input()) for i in range(n)]

if sum(d) % 2 > 0:
    print((-1))
    return

d = sorted([(dd, i) for i, dd in enumerate(d)], reverse=True)
d_to_i = {dd: i for dd, i in d}
n_child = [1] * n
d_child = [0] * n
ans = []
for dd, i in d:
    d_i = dd + 2 * n_child[i] - n
    if d_i in list(d_to_i.keys()):
        i_next = d_to_i[d_i]
        ans.append((i + 1, i_next + 1))
        n_child[i_next] += n_child[i]
        d_child[i_next] += d_child[i] + n_child[i]
        if n_child[i_next] == n:
            break
    else:
        print((-1))
        return

d_min, i_min = d[-1]
if d_min == d_child[i_min]:
    for a in ans:
        print((*a))
else:
    print((-1))
