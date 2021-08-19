def min_value(digits):
    nodupe = list(set(digits))
    j = len(nodupe)
    output = 0
    nodupe.sort()
    for i in nodupe:
        output += i * pow(10, j - 1)
        j -= 1
    return output
