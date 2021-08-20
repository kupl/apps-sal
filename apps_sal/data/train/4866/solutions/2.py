def split_even_number0(n):
    if not n % 4:
        return [n / 2 - 1, n / 2 + 1]
    return [n / 2, n / 2]


def split_even_number1(n):
    return [1, n - 1]


def split_even_number2(n):
    times = 1
    tmp = n
    while not tmp % 2:
        tmp /= 2
        times *= 2
    return [tmp] * times


def split_even_number3(n):
    return [1] * n


def split_all_even_numbers(numbers, way):
    result = []
    for i in numbers:
        if i % 2:
            result += [i]
        elif way == 0:
            result += split_even_number0(i)
        elif way == 1:
            result += split_even_number1(i)
        elif way == 2:
            result += split_even_number2(i)
        else:
            result += split_even_number3(i)
    return result
