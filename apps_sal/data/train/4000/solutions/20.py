from numpy import prod
def strong_num(n):
    return ["Not Strong !!", "STRONG!!!!"][ sum(prod(range(1,i+1)) for i in map(int, str(n)))==n]
