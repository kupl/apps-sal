def calculate(s):
    return str(sum(map(int, s.replace('plus', ' ').replace('minus', ' -').split())))
