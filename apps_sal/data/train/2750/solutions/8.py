def make_sequences(n):
    memo_res = memo.get(n)
    if memo_res:
        return memo_res
        
    count = 1 + sum(make_sequences(x) for x in range(1, n // 2 + 1))
    memo[n] = count
    return count
    
memo = {}
