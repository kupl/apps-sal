def divisors(n):
    count = 1
    for num in range(1, n):
        if (n / num).is_integer() == True:
            count += 1

    return count
