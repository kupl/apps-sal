def power_sumDigTerm(n):
    my_list = []
    for number in range(2, 100):
        for exponent in range(2, 50):
            raised_number = number ** exponent
            sum_of_digits = 0
            for digit in list(str(raised_number)):
                sum_of_digits += int(digit)
            if sum_of_digits ** exponent == raised_number:
                my_list.append(raised_number)
    answer = sorted(my_list)
    return answer[n - 1]
