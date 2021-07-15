def expression_matter(a, b, c):
    cases = [a + b + c]
    cases.append(a * b * c)
    cases.append((a * b) + c)
    cases.append((a + b) * c)
    cases.append(a + (b * c))
    cases.append(a * (b + c))
    return max(cases)
