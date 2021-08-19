def mid(n):
    x = 1 << n.bit_length() - 1
    return x - 1 if x // 2 - 1 <= n - x else n - x // 2


def complete_binary_tree(a):
    (res, queue) = ([], [a])
    while queue:
        L = queue.pop(0)
        m = mid(len(L))
        res.append(L[m])
        if m:
            queue.append(L[:m])
        if m < len(L) - 1:
            queue.append(L[m + 1:])
    return res
