import re


def quicksum(packet):
    isValid = re.match(r'[A-Z ]*$', packet)
    value = sum(i * (ord(c) - 64) for i, c in enumerate(packet, 1) if c != ' ')
    return isValid and value or 0
