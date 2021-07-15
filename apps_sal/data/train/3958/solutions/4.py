def custom_fib(seq, indexes, n):
    size = len(seq)
    
    while len(seq) <= n:
        tail = seq[-size:]
        seq.append( sum( tail[i] for i in indexes ) )
    
    return seq[n]
