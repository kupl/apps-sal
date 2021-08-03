def f(n):
    output = []
    to_add = 0
    for i in range(0, n + 1):
        output.append(2**i)
    output.append(sum(output))
    return output
