
        
def insert_dash(num):
    odd = False
    result = []
    for n in str(num):
        num = n;
        if int(n) % 2 == 0:
            odd = False
        elif odd:
            num = '-' + num
        else:
            odd = True
        
        result.append(num)


        
    return ''.join(result)
