def shifted_diff(first, second):
    for i in range(len(first)):
        if first == second[i:] + second[:i]:
            return i
    return -1
