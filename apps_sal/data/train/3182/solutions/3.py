import math


def LDTA(n):
    if n == 1 or math.log10(n) % 1 == 0:
        return None
    else:
        power = 1
        digits = [d for d in range(0, 10)]
        while digits:
            number = [int(x) for x in str(n ** power)]
            for x in number:
                if x in digits:
                    last_one = x
                    digits.remove(x)
            power += 1
        return last_one
