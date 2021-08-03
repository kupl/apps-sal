import math


def list_squared(m, n):
    divs = []
    answer = []
    for x in range(m, n):
        divs = [1]
        for y in range(2, int(math.sqrt(x)) + 1):
            if x % y == 0 and math.sqrt(x) != y:
                divs.extend([y**2, int((x / y)**2)])
        if x != 1:
            divs.append((x * x))
        z = sum(divs)
        if math.sqrt(z) % 1 == 0:
            answer.append([x, z])
    return answer
