def is_lucky(n):
    sum = 0
    for number in str(n):
        sum += int(number)
    return sum % 9 == 0
