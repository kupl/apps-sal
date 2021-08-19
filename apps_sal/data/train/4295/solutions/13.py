def balanced_num(n):
    n = [int(i) for i in str(n)]
    m = [len(n) // 2 - 1, len(n) // 2] if len(n) % 2 == 0 else [len(n) // 2]   # middle digits positions
    return "Balanced" if sum(n[:m[0]]) == sum(n[m[-1] + 1:]) else "Not Balanced"
