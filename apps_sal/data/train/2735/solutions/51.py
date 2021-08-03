def jumping_number(number):
    num_list = [int(i) for i in str(number)]
    jumping = 'Jumping!!'
    for i in range(len(num_list)):
        if i < len(num_list) - 1 and abs(num_list[i] - num_list[i + 1]) != 1:
            jumping = 'Not!!'
    return jumping
