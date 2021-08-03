t = int(input())

for _ in range(t):
    n = int(input())

    row_count = {}

    for i in range(n):
        s = input()
        row_count[i + 1] = [s[:(n // 2)].count('1'), s[(n // 2):].count('1')]

    left_sum, right_sum = 0, 0
    for val in list(row_count.values()):
        left_sum += val[0]
        right_sum += val[1]

    min_abs_diff = abs(left_sum - right_sum)

    for row, val in list(row_count.items()):
        diff_swap_row = abs(
            (left_sum - val[0] + val[1]) - (right_sum - val[1] + val[0]))
        if diff_swap_row < min_abs_diff:
            min_abs_diff = diff_swap_row

    print(min_abs_diff)
