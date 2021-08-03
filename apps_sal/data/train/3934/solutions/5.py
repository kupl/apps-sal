def pattern(n):
    result = []
    for i in range(n, 0, -1):
        string = ""
        for j in range(n, n - i, -1):
            string += str(j)
        result.append(string)
    return "\n".join(result)
