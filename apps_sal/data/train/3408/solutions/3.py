def add_check_digit(n):
    s = sum(int(n[-1 - i])*(i % 6 + 2) for i in range(len(n)))
    return n + [str(11-s%11),['X','0'][s%11==0]][s%11<2]
