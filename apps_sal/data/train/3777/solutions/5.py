from string import ascii_uppercase

AZ = dict(list(zip(' ' + ascii_uppercase, list(range(27)))))


def quicksum(packet):
    result = 0
    for i, a in enumerate(packet, 1):
        try:
            result += AZ[a] * i
        except KeyError:
            return 0
    return result

