def increment_string(strng):
    num = []
    for alpha in strng[::-1]:
        if alpha.isdigit():
            num.insert(0, alpha)
        else:
            break
    if num and num[0] == '0':
        temp = int(''.join(num)) + 1
        temp = str(temp).zfill(len(num))
        strng = strng[:-len(num)] + temp
    elif num and num[0] != '0':
        temp = int(''.join(num)) + 1
        strng = strng[:-len(num)] + str(temp)
    else:
        strng = strng + '1'
    return strng

