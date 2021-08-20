def solve():
    N = int(input())
    D = [int(input()) for i in range(N)]
    if sum(D) % 2 > 0:
        print('-1')
        return
    Di = sorted([(di, i) for (i, di) in enumerate(D)], key=lambda x: x[0], reverse=True)
    d_to_i = {dd: i for (dd, i) in Di}
    ans = []
    n_child = [1] * N
    d_child = [0] * N
    for (valD, node) in Di:
        valD_par = valD - N + 2 * n_child[node]
        if valD_par in list(d_to_i.keys()):
            node_par = d_to_i[valD_par]
            ans.append((node_par + 1, node + 1))
            n_child[node_par] += n_child[node]
            d_child[node_par] += n_child[node] + d_child[node]
            if n_child[node_par] == N:
                break
        else:
            print('-1')
            return
    (d_min, i_min) = Di[-1]
    if d_child[i_min] != d_min:
        print('-1')
        return
    for (i, j) in ans:
        print(str(i) + ' ' + str(j))


def __starting_point():
    solve()


__starting_point()
