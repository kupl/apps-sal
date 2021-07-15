def solve(st):
    attempts = len(st) // 2
    for i in range(attempts, 0, -1):
        if st[:i] == st[-i:]:
            return i
    return 0
