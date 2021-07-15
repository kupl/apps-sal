def automorphic(number):
    num = number
    squ = num ** 2

    str_num = str(num)
    str_squ = str(squ)

    len_num = len(str_num)
    len_squ = len(str_squ)


    i = len_squ - len_num
    j = 0
    return_value = 0
    for i in range( (len_squ-len_num), len_squ):
        if str_num[j] != str_squ[i]:
            return_value +=1
        i += 1
        j += 1
    if return_value == 0:
        return "Automorphic"
    else:
        return "Not!!"
