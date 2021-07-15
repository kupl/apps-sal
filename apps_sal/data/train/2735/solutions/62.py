def jumping_number(number):
    return 'Jumping!!' if number < 10 or (abs((number % 10) - (number // 10 % 10)) == 1 and jumping_number(number // 10) == 'Jumping!!') else 'Not!!'
