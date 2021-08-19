def factorial(n):
    val = 1
    for i in range(n, 1, -1):
        val *= i
    return val


def strong_num(number):
    return 'STRONG!!!!' if sum((factorial(int(i)) for i in str(number))) == number else 'Not Strong !!'
