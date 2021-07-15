digits = '1234567890' * 1000

def get_a_down_arrow_of(n):
    width = 2 * n - 1
    return '\n'.join(
        ''.join(digits[:i-1] + digits[max(i-1, 0)::-1]).center(width).rstrip()
        for i in range(n, 0, -1)
    )
