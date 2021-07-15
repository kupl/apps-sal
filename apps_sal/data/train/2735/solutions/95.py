def jumping_number(num):
    num = str(num)
    jumping = all(abs(int(a) - int(b)) == 1 for a, b in zip(num[:-1], num[1:]))
    return "Jumping!!" if jumping else "Not!!"
