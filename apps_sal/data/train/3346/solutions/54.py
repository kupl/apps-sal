import math


def gap(g, m, n):
    gap = -1
    in_gap = "N"
    for amiprime in range(m, n):
        end = math.ceil(amiprime**0.5) + 1
#         print(end)
        for divisor in range(2, end):
            if (amiprime % divisor) == 0:
                #                 print(F'{amiprime} is divisible by {divisor}')
                if gap > 0:
                    gap += 1
                break
        else:
            if gap == g:
                #                 print(F'{prevprime} and {amiprime} are prime and this is the first gap of {g}')
                return [prevprime, amiprime]
                break
#             print(F'{amiprime} is prime and the gap since the last prime is {gap}')
            prevprime = amiprime
            gap = 1
    return None
