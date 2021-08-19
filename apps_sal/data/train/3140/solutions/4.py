def happy_numbers(n):
    return [q for q in range(n + 1) if isHappy(q)]


def isHappy(o, lister=[]):
    if len(lister) > len(set(lister)):
        return False
    summer = sum([int(p) ** 2 for p in str(o)])
    return True if summer == 1 else isHappy(summer, lister + [summer])
