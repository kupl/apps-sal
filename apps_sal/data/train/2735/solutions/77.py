def jumping_number(number):
    num = list(map(int, str(number)))
    if all(abs(x - y) == 1 for x, y in zip(num, num[1:])):
        return "Jumping!!"
    else:
        return "Not!!"
