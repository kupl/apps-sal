def josephus(n, k):
    i, ans = 0, []
    while n:
        i = (i + k - 1) % len(n)
        ans.append(n.pop(i))
    return ans
