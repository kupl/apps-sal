import math


def gap(g, m, n):
    gap = -1
    in_gap = 'N'
    for amiprime in range(m, n):
        end = math.ceil(amiprime ** 0.5) + 1
        for divisor in range(2, end):
            if amiprime % divisor == 0:
                if gap > 0:
                    gap += 1
                break
        else:
            if gap == g:
                return [prevprime, amiprime]
                break
            prevprime = amiprime
            gap = 1
    return None
