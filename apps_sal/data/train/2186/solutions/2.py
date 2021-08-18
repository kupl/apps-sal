MOD = 10**9 + 7


def topo_compute(childrens, colors, parents):
    def f(node, connected_to_black):
        if colors[node] == 1 and connected_to_black:
            return 0

        children = childrens[node]
        if colors[node] == 1 or connected_to_black:
            ret = 1

            for child in children:
                x = dp_conn[child] + dp_not_conn[child]
                x %= MOD

                ret *= x
                ret %= MOD

            return ret

        s = 1
        prefix_prod = []
        for child in children:
            x = dp_conn[child] + dp_not_conn[child]
            x %= MOD
            s *= x
            s %= MOD
            prefix_prod.append(s)

        s = 1
        suffix_prod = []
        for child in reversed(children):
            x = dp_conn[child] + dp_not_conn[child]
            x %= MOD
            s *= x
            s %= MOD
            suffix_prod.append(s)

        suffix_prod = list(reversed(suffix_prod))

        ret = 0

        for i in range(len(children)):
            pre = prefix_prod[i - 1] if i > 0 else 1
            suf = suffix_prod[i + 1] if i + 1 < len(suffix_prod) else 1

            x = pre * suf
            x %= MOD

            x *= dp_not_conn[children[i]]
            x %= MOD

            ret += x
            ret %= MOD

        return ret

    num_childrens = [len(x) for x in childrens]
    N = len(childrens)
    dp_conn = [None] * N
    dp_not_conn = [None] * N

    stack = [i for i in range(N) if num_childrens[i] == 0]

    while True:
        node = stack.pop()

        dp_conn[node] = f(node, True)
        dp_not_conn[node] = f(node, False)

        parent = parents[node]

        if parent is None:
            return dp_not_conn[node]

        num_childrens[parent] -= 1
        if num_childrens[parent] == 0:
            stack.append(parent)


def build_tree(d, root):
    childrens = [None] * len(d)
    parents = [None] * len(d)

    stack = [(root, None)]

    while len(stack) > 0:
        node, parent = stack.pop()

        children = [x for x in d[node] if x != parent]

        childrens[node] = children
        parents[node] = parent

        for child in children:
            stack.append((child, node))

    return childrens, parents


def main():
    import sys

    n = sys.stdin.readline()
    n = int(n)

    p = list(map(int, sys.stdin.readline().split(" ")))

    d = {}

    for i in range(n):
        d[i] = []

    for i, b in enumerate(p):
        a = i + 1
        d[a].append(b)
        d[b].append(a)

    colors = list(map(int, sys.stdin.readline().split(" ")))
    colors = list(colors)

    for i in range(n - 1):
        line = sys.stdin.readline()
        if line == "":
            break

        a, b = list(map(int, line.split(" ")))

        d[a].append(b)
        d[b].append(a)

    childrens, parents = build_tree(d, 0)

    ans = topo_compute(childrens, colors, parents)
    print(ans)


def __starting_point():
    main()


__starting_point()
