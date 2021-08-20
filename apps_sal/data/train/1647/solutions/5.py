def next_bigger(n):
    prefix = list(str(n))
    postfix = [prefix.pop()]
    while prefix and prefix[-1] >= max(postfix):
        postfix.append(prefix.pop())
    if not prefix:
        return -1
    postfix.sort()
    i = next((i for (i, d) in enumerate(postfix) if d > prefix[-1]))
    (postfix[i], prefix[-1]) = (prefix[-1], postfix[i])
    return int(''.join(prefix + postfix))
