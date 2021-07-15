def check_valid_tr_number(number):
    print(number)
    if not len(str(number)) == 11 or not isinstance(number, int):
        return False
    
    number = str(number)
    odd = int(number[0])+int(number[2])+int(number[4])+int(number[6])+int(number[8])
    even = int(number[1])+int(number[3])+int(number[5])+int(number[7])
    
    sub = ((odd*7)-even)%10
    
    if str(sub) == number[9] and (((odd+even+int(number[9])) %10) == int(number[10])):
        return True
    else:
        return False
