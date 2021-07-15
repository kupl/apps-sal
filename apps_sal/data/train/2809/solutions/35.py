def digitize(n):
    result = []
    for d in str(n)[::-1]:
        result.append(int(d))
    return result
