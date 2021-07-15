def digitize(n):
    results = []
    for num in str(n)[::-1]:
        results.append(int(num))
    return results
