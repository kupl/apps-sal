def odd_one_out(s):
    memo = {}
    for c in s:
        if c in memo:
            del memo[c]
        else:
            memo[c] = None
    return list(memo.keys())
