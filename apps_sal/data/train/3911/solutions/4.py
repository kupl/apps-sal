def howmuch(m, n):
    return [[f'M: {M}', f'B: {M // 7}', f'C: {M // 9}'] for M in range(min(m, n), max(m, n) + 1) if M % 7 == 2 and M % 9 == 1]
