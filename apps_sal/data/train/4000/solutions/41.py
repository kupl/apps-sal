def strong_num(number):
    sm=0
    for num in str(number):
        fact = 1
        for en in range(1,int(num)+1):
            fact *=en
        sm+= fact
    if sm == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
