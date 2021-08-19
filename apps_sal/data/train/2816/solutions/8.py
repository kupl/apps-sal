def calculate(s):
    # your code here
    return str(sum(map(int, s.replace('plus', ' ').replace('minus', ' -').split())))
