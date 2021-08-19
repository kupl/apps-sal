def dig_sum(n):
    return sum(map(int, str(n)))


def solve(n):
    candidates = [n] + [n // 10 ** i * 10 ** i - 1 for i in range(1, len(str(n)))]
    return max(candidates, key=dig_sum)
