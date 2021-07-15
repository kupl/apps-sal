def solve(st):
    return next((n for n in range(len(st)//2, 0, -1) if st[:n] == st[-n:]), 0)

