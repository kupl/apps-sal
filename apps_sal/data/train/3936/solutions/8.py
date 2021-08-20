def zozonacci(pattern, length):
    if length == 0:
        return []
    if pattern == []:
        return []
    result = [0, 0, 0, 1] if pattern[0] != 'pad' else [0, 1, 0, 0]
    result2 = []
    if length < 4:
        for i in range(length):
            result2.append(result[i])
        return result2
    j = 0
    for i in range(4, length):
        seq = pattern[j]
        if seq == 'fib':
            result.append(result[i - 1] + result[i - 2])
        elif seq == 'jac':
            result.append(result[i - 1] + 2 * result[i - 2])
        elif seq == 'pad':
            result.append(result[i - 2] + result[i - 3])
        elif seq == 'pel':
            result.append(2 * result[i - 1] + result[i - 2])
        elif seq == 'tet':
            result.append(result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4])
        else:
            result.append(result[i - 1] + result[i - 2] + result[i - 3])
        j += 1
        if j == len(pattern):
            j = 0
    return result
