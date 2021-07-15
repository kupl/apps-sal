def sum_of_n(n):
    output = [0]
    sign = 1
    if n < 0: sign = -1
    for numb in range(1, abs(n) + 1):
        output.append(sign * (numb + abs(output[numb - 1])))
    return output
