def f(n):
    result = [1]
    for i in range(n):
        result.append(result[-1]*2)
    result.append(sum(result))
    return result
