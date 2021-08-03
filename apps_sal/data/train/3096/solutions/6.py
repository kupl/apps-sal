def josephus(n, k):
    k -= 1
    i = k

    result = []
    while n:
        if i < len(n):
            result.append(n.pop(i))
            i += k
        else:
            while i >= len(n):
                i -= len(n)
    return result
