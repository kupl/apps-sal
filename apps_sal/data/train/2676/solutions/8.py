def find_needed_guards(k):
    total = 0
    for i in range(1, len(k)):
        if not (k[i] or k[i-1]):
            k[i] = True
            total += 1
    return total
