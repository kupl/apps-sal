def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def strong_num(number):
    result=0
    numLst=[int(x) for x in str(number)]
    for i in range(len(numLst)):
        result+=factorial(numLst[i])
    return "STRONG!!!!" if result==number else "Not Strong !!"
