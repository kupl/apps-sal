def solve(a, b):
    number_counter = 0
    for i in range(a, b):
        number = str(i)
        if '0' in number or '1' in number or '2' in number or ('4' in number) or ('6' in number) or ('7' in number) or ('9' in number):
            continue
        a = number.count('3')
        b = number.count('5')
        c = number.count('8')
        if a + b + c == len(number) and a <= b and (b <= c):
            number_counter += 1
    return number_counter
