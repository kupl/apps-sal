def any_odd(x):
    binary = bin(x)
    answer = 0
    binary_reversed = str(binary[::-1])
    for k in range(0, len(binary_reversed)):
        if k % 2 != 0 and binary_reversed[k] == '1':
            answer = 1
    return answer
