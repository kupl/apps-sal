anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def solution(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)
