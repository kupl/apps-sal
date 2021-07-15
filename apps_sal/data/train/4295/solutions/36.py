def balanced_num(number):
    return 'Balanced' if sum(int(n) for n in str(number)[:len(str(number))//2+1]) == sum(int(n) for n in str(number)[::-1][:len(str(number))//2+1]) else 'Not Balanced'
