def arithmetic_sequence_elements(a, r, n):
    result = str(a)
    list_ = [a]
    for i in range(n - 1):
        result += ', ' + str(list_[-1] + r)
        list_.append(list_[-1] + r)
    return result
