import math
def decompose(n):
    if n <= 4: return None
    result = [n - 1]
    remain = n ** 2 - (n - 1) ** 2
    while True:
        if not remain: return list(reversed(result))
        if result[0] == 1: return None
        if result[-1] == 1:
            remain += result.pop() ** 2
            result[-1] -= 1
            remain += (result[-1] + 1) ** 2 - result[-1] ** 2
        else:
            i = min(result[-1] - 1, int(math.floor(math.sqrt(remain))))
            result.append(i)
            remain -= i ** 2
