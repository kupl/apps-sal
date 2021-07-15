from math import ceil

def union_jack(n):
    if not isinstance(n, (int, float)):
        return False
    n = max(7, ceil(n))
    h, m = divmod(n-1, 2)
    flag = [["X" if len({i, n-j-1, j, h, h+m}) < 4+m else "-" for i in range(n)] for j in range(n)] 
    return "\n".join("".join(row) for row in flag)
