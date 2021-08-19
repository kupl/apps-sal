def check_concatenated_sum(number, n):
    return (10 ** n - 1) // 9 * sum(map(int, str(abs(number)))) == abs(number)
