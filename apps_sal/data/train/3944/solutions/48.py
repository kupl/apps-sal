def sum_triangular_numbers(n):
    numberz = 0
    triangular_numbers = []
    if n <= 0:
        return 0
    else:
        number = 0
        for int in range(0, n + 1):
            number = number + int
            triangular_numbers.append(number)
    for num in triangular_numbers:
        numberz = numberz + num

    return numberz
