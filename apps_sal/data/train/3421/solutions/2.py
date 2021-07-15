def mysterious_pattern(size, n, fib=1, tmp=0):
    rows = [ [" "] * size for _ in range(n) ]
    
    for idx in range(size):
        rows[fib % n][idx] = "o"
        tmp, fib = fib, fib + tmp
    
    return "\n".join( "".join(row).rstrip() for row in rows ) .strip("\n")
