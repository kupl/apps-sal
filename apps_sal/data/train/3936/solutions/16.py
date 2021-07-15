def zozonacci(pattern, length):
    if length == 0 or pattern == []:
        return []
    result = {
        "fib": [0, 0, 0, 1],
        "jac": [0, 0, 0, 1],
        "pad": [0, 1, 0, 0],
        "pel": [0, 0, 0, 1],
        "tet": [0, 0, 0, 1],
        "tri": [0, 0, 0, 1]
    }[pattern[0]]
    if length < 4:
        result = result[:length]
        return result
    i = 0
    j = 4
    while len(result) < length:
        r = {
            "fib": result[j - 1] + result[j - 2],
            "jac": result[j - 1] + 2 * result[j - 2],
            "pad": result[j - 2] + result[j - 3],
            "pel": 2 * result[j - 1] + result[j - 2],
            "tet": result[j - 1] + result[j - 2] + result[j - 3] + result[j - 4],
            "tri": result[j - 1] + result[j - 2] + result[j - 3]
        }[pattern[i]]
        result.append(r)
        i = (i + 1) % len(pattern)
        j += 1
    return result
