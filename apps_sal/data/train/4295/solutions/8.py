def balanced_num(number):
    d = list(map(int, str(number)))
    part = (len(d)-1)//2
    return 'Not '*(sum(d[:part]) != sum(d[-part:]) and len(d) > 2) + 'Balanced'
