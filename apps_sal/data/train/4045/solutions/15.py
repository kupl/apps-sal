def number(lines):
    ans = []
    for x in range(1, len(lines) + 1):
        ans.append(f'{x}: {lines[x - 1]}')
    return ans
