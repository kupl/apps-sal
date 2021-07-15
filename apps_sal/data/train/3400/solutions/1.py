def even_numbers(arr, n):
    result = []
    a = list(reversed(arr))
    for number in a:
        if n == 0:
            break
        if number % 2 == 0:
            result.append(number)
            n -= 1
    return list(reversed(result))
