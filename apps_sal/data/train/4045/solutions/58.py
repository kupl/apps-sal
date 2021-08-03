def number(lines):
    return [f"{num}: {line}" for num, line in zip([i for i in range(1, len(lines) + 1)], lines)]
