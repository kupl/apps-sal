def order_weight(strng):
    result = 0
    solution = []
    numbers_list = [int(x) for x in strng.split()]
    for x in numbers_list:
        while x > 0:
            result += x % 10
            x = x // 10
        solution.append(result)
        result = 0
    return ' '.join([x for _, x in sorted(zip(solution, [str(x) for x in numbers_list]))])
