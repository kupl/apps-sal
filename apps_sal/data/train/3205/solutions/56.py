def is_divisible(n, x, y):
    answer = n / x
    answer2 = n / y
    answer_integer_check = answer.is_integer()
    answer2_integer_check = answer2.is_integer()
    if answer_integer_check and answer2_integer_check == True:
        return True
    else:
        return False
