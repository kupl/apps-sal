def find_digit(num, nth):
    
    if nth <= 0:
        return -1 
    else: 
        num = str(num)
        num_digits = ""

        for x in num:
            if x != "-":
                num_digits += x

        if len(num_digits) < nth:
            return 0
        else:
            nth = nth * -1
            result = num[nth]
            return int(result)
