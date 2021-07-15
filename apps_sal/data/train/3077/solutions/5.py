def pattern(n):
    output = ""
    for i in range(1, n+1):
        for j in range(i, n+1):
            output += str(j)
        if i < n:
            output += '\n'
    return output
