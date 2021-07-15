def pattern(n):
    return "\n".join("".join(str(j) for j in range(n, n-i, -1)) for i in range(1, n+1))
