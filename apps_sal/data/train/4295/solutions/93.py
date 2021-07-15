def balanced_num(number):
    number = str(number)
    str_sum = lambda xs: sum(map(int,xs))
    return 'Balanced' if str_sum(number[:(len(number)-1)//2]) == str_sum(number[(len(number)+2)//2:]) else 'Not Balanced'
