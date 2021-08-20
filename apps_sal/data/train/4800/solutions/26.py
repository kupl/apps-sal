def hotpo(start, memo={2: 1}):
    """ uses memoization """
    n = start
    seq_l = 0
    while n > 1:
        if memo.get(n, False):
            if n != start:
                memo[start] = memo[n] + seq_l
            return memo[n] + seq_l
        if n % 2 == 0:
            n = n // 2
            seq_l += 1
        else:
            n = (n * 3 + 1) // 2
            seq_l += 2
    return 0
