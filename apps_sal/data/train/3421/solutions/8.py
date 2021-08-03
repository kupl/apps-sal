def mysterious_pattern(m, n):
    # get the fibonacci sequence:
    fib = [1, 1]
    for i in range(m - 2):
        fib.append(fib[-1] + fib[-2])
    # get a 2d array of chars based on the fibonacci mod results:
    ret = [["o" if fib[x] % n == y else " " for x in range(m)] for y in range(n)]
    # convert the 2d array to string form:
    return "\n".join("".join(row).rstrip() for row in ret).strip("\n")
