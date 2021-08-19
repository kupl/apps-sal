(cost, res) = ({}, [])
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    if len(arr) == 4:
        (_, u, v, w) = arr
        while u != v:
            if u > v:
                cost[u] = cost.get(u, 0) + w
                u //= 2
            else:
                cost[v] = cost.get(v, 0) + w
                v //= 2
    else:
        (_, u, v) = arr
        curr_res = 0
        while u != v:
            if u > v:
                curr_res += cost.get(u, 0)
                u //= 2
            else:
                curr_res += cost.get(v, 0)
                v //= 2
        res.append(str(curr_res))
print('\n'.join(res))
