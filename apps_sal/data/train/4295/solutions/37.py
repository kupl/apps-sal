def balanced_num(number):
    if number < 100:
        return "Balanced"
    
    if len(str(number))%2:
        x = str(number)[:len(str(number))//2]
        y = str(number)[len(str(number))//2+1:]
        return 'Balanced' if sum([int(i) for i in x])==sum([int(i) for i in y]) else 'Not Balanced'

    elif not len(str(number))%2:
        x = str(number)[:len(str(number))//2-1]
        y = str(number)[len(str(number))//2+1:]
        return 'Balanced' if sum([int(i) for i in x])==sum([int(i) for i in y]) else 'Not Balanced'
