def distinct_digit_year(year):
    next_year = int(year)
    while True:
        sum = 0
        next_year = next_year + 1
        for num in str(next_year):
            sum += str(next_year).count(num)
        if sum == 4:
            break
    return next_year
