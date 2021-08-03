def extra_perfect(n):
    return [i for i in range(1, n + 1) if bin(i)[2] == '1' and bin(i)[-1] == '1']
