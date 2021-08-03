primes = {11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
endings = {'00', '01', '25', '76'}


def solve(a, b):
    if b < 1176:
        return 0
    output = 0
    if a < 1176:
        a = 1176
    for i in [x for x in range(a, b) if str(x)[-2:] in endings]:
        if int(str(i)[:2]) not in primes:
            continue
        if int(str(i * i)[:2]) in primes:
            output += 1
    return output
