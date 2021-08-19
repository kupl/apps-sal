import sys


def dfs(tree, root, priv_root, cur_lvl, priv_lvl, diff, pick_list):
    # if tree is 1 or less nodes just return nothing
    if not tree:
        return
    stack = [(root, priv_root, cur_lvl, priv_lvl)]
    while stack:
        (root, priv_root, cur_lvl, priv_lvl) = stack.pop()
        # set level to account for only evens where a difference exists
        if cur_lvl ^ diff[root]:
            cur_lvl ^= 1
            pick_list.append(str(root))
        # add to the queue all cases where a vertex exists
        stack += [(vertex, root, priv_lvl, cur_lvl)
                  for vertex in tree[root] if vertex != priv_root]


def main():
    n = int(input())
    tree = dict()
    for _ in range(n - 1):
        u, v = [int(x) for x in input().split()]
        tree[u] = tree.get(u, set()) | set([v])
        tree[v] = tree.get(v, set()) | set([u])
    init = [0] + [int(x) for x in input().split()]
    goal = [0] + [int(x) for x in input().split()]
    # find numbers that don't match that need to be accounted for
    diff = [i ^ j for (i, j) in zip(init, goal)]
    pick_list = list()

    dfs(tree, 1, 0, 0, 0, diff, pick_list)

    num = len(pick_list)
    print(num)
    if num:
        print('\n'.join(pick_list))


def __starting_point():
    return(main())


__starting_point()
