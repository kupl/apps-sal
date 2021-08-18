def dont_give_me_five(start, end):
    def goo(n):
        result = 0
        pos9 = 1
        while n > 0:
            digit = n % 10
            effective_digit = digit
            if digit > 5:
                effective_digit -= 1
            to_add = effective_digit * pos9
            if digit == 5:
                result = -1
            result += to_add
            n //= 10
            pos9 *= 9
        return result
    if (end >= 0 and start >= 0) or (end < 0 and start < 0):
        return goo(max(abs(end), abs(start))) - goo(min(abs(start), abs(end)) - 1)
    else:
        return goo(abs(end)) + goo(abs(start)) + 1
