def simplify(number):
    num = str(number)
    result = []
    for i, d in enumerate(num, start=1):
        if d == "0":
            continue
        elif i == len(num):
            result.append(d)
        else:
            result.append(d + "*" + "1" + "0" * (len(num) - i))
    return "+".join(result)

