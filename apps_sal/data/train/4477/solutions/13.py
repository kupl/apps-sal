def reverse_number(n):
    if n < 0:
        return int(n.__str__()[1:][::-1]) * -1
    else:
        return int(n.__str__()[::-1])
