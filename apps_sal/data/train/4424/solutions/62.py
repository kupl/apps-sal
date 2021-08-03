def expression_matter(a, b, c):
    x = [a, b, c]
    results = []

    results.append(a * b * c)
    results.append(a * (b + c))
    results.append((a + b) * c)
    results.append(a + b + c)

    return max(results)
