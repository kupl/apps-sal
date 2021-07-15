def factorial(n):
    acc = 1
    for i in range(1, n+1):
        acc = acc * i
    return acc

def strong_num(num):
    rs = list(map(int, str(num)))
    r = [factorial(i) for i in rs]
    return "STRONG!!!!" if sum(r) == num else "Not Strong !!"
    


