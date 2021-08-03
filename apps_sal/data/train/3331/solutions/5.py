def solve(d, pos):
    for i, j in enumerate(d):
        if j == 'D':
            left = next((k for k in range((i - pos) if i - pos > -1 else 0, i) if d[k] == 'C'), -1)
            right = next((k for k in range(i, (i + pos + 1) if i + pos < len(d) else len(d)) if d[k] == 'C'), -1)
            if left != -1:
                d[left] = '.'
            elif right != -1:
                d[right] = '.'
    return d.count('.')
