def colorful(number):
    base_result = []
    for x in str(number):
        base_result.append(int(x))
    for y in range(len(base_result) - 1):
        temp = base_result[y] * base_result[y + 1]
        base_result.append(temp)
    return len(set(base_result)) == len(base_result)
