from math import factorial


def strong_num(number):
    print(number)
    a = str(number)
    count = 0
    for i in range(len(a)):
        if i != len(a):
            count += factorial(int(a[i]))
    print(count)
    return 'STRONG!!!!' if count == number else 'Not Strong !!'
