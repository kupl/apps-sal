def dont_give_me_five(start, end):
    if start < 0 and end < 0:
        return nums_without_five(-start + 1) - nums_without_five(-end)
    elif start < 0 and end >= 0:
        return nums_without_five(-start + 1) + nums_without_five(end + 1) - 1
    return nums_without_five(end + 1) - nums_without_five(start)


def nums_without_five(n):
    cnt = 0
    fct = 1

    while n:
        dig = n % 10
        if dig == 5:
            cnt = 0
        cnt += (dig - (dig > 5)) * fct
        fct *= 9
        n //= 10

    return cnt
