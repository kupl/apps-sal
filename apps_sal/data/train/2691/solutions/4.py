def solve(s):
    result = [0]
    for c in s:
        if '0' <= c <= '9':
            result[-1] = result[-1] * 10 + int(c)
        elif result[-1] > 0:
            result.append(0)
    return max(result)
