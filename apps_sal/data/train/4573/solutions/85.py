def over_the_road(address, n):
    answer = 0
    if address % 2 == 0:
        steps = n - (address / 2)
        answer = 1 + (2 * steps)
    else:
        steps = (n * 2) - address
        answer = steps + 1
    return answer
