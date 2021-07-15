from collections import deque
def array_leaders(numbers):
    res = deque([])
    sm = 0
    i = len(numbers) - 1
    while i >= 0:
        n = numbers[i]
        if n > sm:
            res.appendleft(n);
        sm += n
        i -= 1
    return list(res)
