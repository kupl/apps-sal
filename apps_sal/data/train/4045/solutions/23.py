def number(lines):
    if len(lines) == 0:
        return []

    results = []
    for i, value in enumerate(lines, start=1):
        results.append(str(i) + ": " + value)
    return results
