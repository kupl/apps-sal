def solve(st):
    return max((i for i in range(1, len(st) // 2 + 1) if st[:i] == st[-i:]), default=0)
