def recaman(n):
    s = set()
    prev = 0
    curr = 0
    for i in range(1, n + 1):
        curr = prev - i
        if curr <= 0 or curr in s:
            curr = prev + i
        s.add(curr)
        prev = curr
    return curr
