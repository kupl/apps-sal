def strong_num(number):
    def fact(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return n * fact(n - 1)
    if sum(fact(int(i))for i in str(number)) == number:
        return "STRONG!!!!"
    return "Not Strong !!"
