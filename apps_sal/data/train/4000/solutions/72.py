def strong_num(number):

    res = []
    for x in str(number):
        num = 1
        for y in range(1, int(x)+1):
            num *= y
        res.append(num)

    return "STRONG!!!!" if sum(res) == number else "Not Strong !!"
