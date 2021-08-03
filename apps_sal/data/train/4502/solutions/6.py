def tribonacci(signature, n):
    result = []
    if n > 3:
        result = signature
        for i in range(0, n - 3):
            nextTrib = result[0 + i] + result[1 + i] + result[2 + i]
            print(nextTrib)
            result.append(nextTrib)
    elif n == 3:
        result = signature
    elif n == 2:
        result = [signature[0], signature[1]]
    elif n == 1:
        result = [signature[0]]
    return result
