def correct(m, n, bits):
    failed_row, failed_col = -1, -1
    for row in range(m):
        if sum(int(c) for c in bits[row * n:(row + 1) * n]) % 2 != int(bits[m * n + row]):
            failed_row = row
            break
    for col in range(n):
        if sum(int(bits[j]) for j in range(col, len(bits) - n - m, n)) % 2 != int(bits[m * n + m + col]):
            failed_col = col
            break
    if (failed_row, failed_col) == (-1, -1):
        return bits
    elif failed_row != -1 and failed_col != -1:
        index = n * failed_row + failed_col
    elif failed_row != -1:
        index = m * n + failed_row
    else:
        index = m * n + m + failed_col
    return bits[:index] + str(1 - int(bits[index])) + bits[index + 1:]
