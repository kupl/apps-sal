def dig_pow(n, p):
    digit_power = sum(int(x)**pw for pw, x in enumerate(str(n), p))
    if digit_power % n == 0:
        return digit_power / n
    return -1
