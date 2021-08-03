def jumping_number(number):
    str_list = list(str(number))
    length = len(str_list)
    if length == 1:
        choose = 'Jumping!!'
    elif length == 2:
        if abs(int(str_list[0]) - int(str_list[1])) == 1:
            choose = 'Jumping!!'
        else:
            choose = 'Not!!'
    else:
        for i in range(len(str_list) - 1):
            if abs(int(str_list[i]) - int(str_list[i + 1])) != 1:
                choose = 'Not!!'
                break
            else:
                choose = 'Jumping!!'
    return choose
