""" keep track of numbers checked """
NUMS = [0, 0]


def mult_primefactor_sum(a, b):
    """ only check numbers greater than before """
    for n in range(len(NUMS), b + 1):
        (x, div, factors) = (n, 2, [])
        ' generate prime factors '
        while x > 1:
            if x % div == 0:
                factors.append(div)
                x //= div
            else:
                div += 1 if div == 2 else 2
        ' store number if it fulfills the conditions, otherwise put 0 '
        if len(factors) == 1 or n % sum(factors) != 0:
            NUMS.append(0)
        else:
            NUMS.append(n)
    ' return the results '
    return [x for x in NUMS[a:b + 1] if x]
