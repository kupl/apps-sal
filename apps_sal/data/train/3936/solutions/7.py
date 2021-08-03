def zozonacci(pattern, length):
    if (pattern == [] or length == 0):
        return []

    pattern_dict = {"fib": fibonacci,
                    "jac": jacobsthal,
                    "pad": padovan,
                    "pel": pell,
                    "tet": tetranacci,
                    "tri": tribonacci}
    initial_pattern = pattern[0]

    if (initial_pattern in ["fib", "jac", "pel", "tet", "tri"]):
        resultList = [0, 0, 0, 1]
    else:
        resultList = [0, 1, 0, 0]
    if (length < 4):
        return resultList[:length]

    for x in range(length - 4):
        rule = pattern[x % len(pattern)]
        pattern_dict[rule](resultList)
    return resultList


def fibonacci(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 1] + numbers[n - 2])


def jacobsthal(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 1] + 2 * numbers[n - 2])


def padovan(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 2] + numbers[n - 3])


def pell(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 1] * 2 + numbers[n - 2])


def tetranacci(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 1] + numbers[n - 2] + numbers[n - 3] + numbers[n - 4])


def tribonacci(numbers):
    n = len(numbers)
    numbers.append(numbers[n - 1] + numbers[n - 2] + numbers[n - 3])
