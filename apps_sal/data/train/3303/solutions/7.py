def div_con(x):
    # your code here
    num = 0  # set the variable num = 0
    strnum = 0  # set the variable strnum = 0
    for number in x:  # for an element of x
        if int(number) == number:  # if the integer version of the element is equivalent to the element
            num = num + number  # num is num + the number(element) of x
        else:
            strnum = strnum + int(number)  # otherwise, if it's a string, add the integer value of the string
    num = num - strnum  # num is the total of the integers - the total of the strings
    return num  # return num
