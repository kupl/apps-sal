def remove_smallest(n):
    return (lambda i: n[:i] + n[i + 1:])(n.index(min(n)) if len(n) else 0)
