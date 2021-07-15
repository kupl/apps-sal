def check_digit(number, index1, index2, digit):
    number=str(number)
    if index1<index2:
        index2=index2+1
        return str(digit) in number[index1:index2]
    elif index2<index1:
        index1=index1+1
        return str(digit) in number[index2:index1]
    elif index1==index2 and str(digit)==number[index1]:
        return True
    else:
        return False
