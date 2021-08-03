def rule30(li, n):
    for i in range(n):
        li = [0] + li + [0]
        li = [(li[k - 1] if k else 0) ^ (l or (li[k + 1] if k < len(li) - 1 else 0)) for k, l in enumerate(li)]
    return li
