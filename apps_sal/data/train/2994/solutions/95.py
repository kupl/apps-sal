def find_digit(num, nth):
    #your code here
    if nth>len(str(abs(num))) : return 0
    if nth>0 : return int(str(abs(num))[::-1][nth-1])
    else : return -1
