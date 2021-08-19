def square_sum(numbers):
    sq_nums = []
    for num in numbers:
        sq_nums.append(num ** 2)
    return sum(sq_nums)
