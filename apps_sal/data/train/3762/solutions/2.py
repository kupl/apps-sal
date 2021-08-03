from collections import deque


def pattern(n):
    result = []
    line = deque([str(num) for num in range(1, n + 1)])
    for i in range(n):
        result.append("".join(line))
        line.rotate(-1)
    return "\n".join(result)
