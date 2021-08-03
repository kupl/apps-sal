def late_clock(digits):
    res, digits = [], digits[:]

    def rec(i):
        if i == 3:
            res.append(digits.pop())
            return True
        maxi = 2 if i == 0 else 5 if i == 2 else 3 if res[0] == 2 else 9
        for x in range(maxi, -1, -1):
            if x in digits:
                res.append(digits.pop(digits.index(x)))
                if rec(i + 1):
                    return True
                digits.append(res.pop())
        return False

    rec(0)
    return "{}{}:{}{}".format(*res)
