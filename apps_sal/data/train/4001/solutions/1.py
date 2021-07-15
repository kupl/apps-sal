def dot(n,m):
    result = [("+---" * n) + "+" + "\n" + ("| o " * n) + "|" for i in range(m)]
    result.append(("+---" * n) + "+")
    return "\n".join(result)
