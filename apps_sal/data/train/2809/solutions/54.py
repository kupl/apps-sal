def digitize(n):
    results = []
    for x in range(len(str(n))):
        results.append(int(str(n)[len(str(n)) - x - 1]))
    return results
