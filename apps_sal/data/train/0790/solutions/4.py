def bitadd(tree, index, value):
    index += 1
    while index < len(tree):
        tree[index] += value
        index += index & (-index)


def bitsum(tree, index):
    index += 1
    result = 0
    while index:
        result += tree[index]
        index -= index & (-index)
    return result


n, m, c = list(map(int, input().split()))
tree = [0 for _ in range(n + 1)]
for _ in range(m):
    q = input().split()
    if q[0] == "Q":
        print(bitsum(tree, int(q[1]) - 1) + c)
    else:
        u = int(q[1])
        v = int(q[2])
        k = int(q[3])
        bitadd(tree, u - 1, k)
        bitadd(tree, v, -k)
