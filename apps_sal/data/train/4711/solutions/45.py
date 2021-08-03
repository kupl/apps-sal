def zeros(n):
    count = 0

    divider = 5

    while (n / divider >= 1):
        count += int(n / divider)
        divider *= 5
    return int(count)
