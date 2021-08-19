def disarium_number(number):
    number_word = str(number)
    count = 1
    cur_sum = 0
    for i in str(number):
        cur_sum = cur_sum + int(i) ** count
        count += 1
    if cur_sum == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
