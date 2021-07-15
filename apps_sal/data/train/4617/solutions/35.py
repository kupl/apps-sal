def powers_of_two(n):
    if n == 0:
        return [1]
    else: 
        result = []
        for x in range(n+1):
            result.append(2**x)
        return result
