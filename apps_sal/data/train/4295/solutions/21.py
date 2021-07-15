def balanced_num(number):
    n = (len(str(number)) - 1) // 2
    return 'Balanced' if n <= 0 or sum(int(i) for i in str(number)[:n]) == sum(int(j) for j in str(number)[-n:]) else 'Not Balanced'
