def get_num(arr):
    if len(arr) == 0:
        return []

    res = 1
    smallest = arr[0]
    divisors = {}
    for val in arr:
        res *= val

        if val < smallest:
            smallest = val

        if val not in divisors:
            divisors[val] = 0
        divisors[val] += 1

    num_divisors = 1
    for val in divisors:
        num_divisors *= (divisors[val] + 1)

    return [res, num_divisors - 1, smallest, res // smallest]
