def luxhouse(a):
    li = []
    for (i, j) in enumerate(a[:-1]):
        right = max(a[i + 1:])
        li.append(0 if j > right else right - j + 1 if right != j else 1)
    return li + [0]
