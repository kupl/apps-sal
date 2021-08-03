def shifted_diff(first, second):
    genexp = [i for i in range(len(second)) if first == second[i:] + second[:i]]
    if genexp:
        return max(genexp)
    return -1
