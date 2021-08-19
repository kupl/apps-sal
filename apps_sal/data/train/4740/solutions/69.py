def row_sum_odd_numbers(n):
    if n == 1:
        return 1
    else:
        nums = list(range(sum(range(n * 2))))
        val = sum(range(n))
        return sum(list((num for num in nums if num % 2 != 0))[val:val + n])
