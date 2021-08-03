def combs(a, b):
    return min(mesh(a, b), mesh(b, a))


def mesh(a, b):
    for i in range(len(a)):
        for j, k in zip(a[i:], b):
            if j + k == '**':
                break
        else:
            return max(i + len(b), len(a))
    return len(a) + len(b)
