def jumping_number(number):
    num_list = list(map(int,list(str(number))))
    for i in range(1,len(num_list)):
        if abs(num_list[i] - num_list[i-1]) != 1:
            return "Not!!"
    return "Jumping!!"
