def balanced_num(n):
    if n < 100:
        return 'Balanced'
    n = [int(i) for i in str(n)]
    return 'Balanced' if sum(n[:int(len(n) / 2) - 1 + len(n) % 2]) == sum(n[int(len(n) / 2) + 1:]) else 'Not Balanced'
