def make_negative(number):
    for num in [int(number)]:
        if num <= 0:
            return(num)
        if num > 0:
            return abs(number) * -1
