PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def square_pi(digits):
    n = 100 - digits + 1
    num = PI // 10**n
    sum = 0
    while num:
        num, m = divmod(num, 10)
        sum += m**2
    i = 0
    while True:
        if i**2 >= sum:
            return i
        i += 1

