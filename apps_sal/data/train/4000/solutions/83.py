def strong_num(number):
    number_list = [int(i) for i in str(number)]
    strong_list = []
    for i in number_list:
        res = 1
        for i in range(1, i + 1):
            res *= i
        strong_list.append(res)
    return 'STRONG!!!!' if sum(strong_list) == number else 'Not Strong !!'
