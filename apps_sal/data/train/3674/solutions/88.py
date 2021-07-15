def add_binary(a,b):
    sum = a + b
    msg = []
    y = sum
    while y > 1:
        y = y // 2
        msg.insert(0, str(y % 2))

    msg.append(str(sum % 2))

    return "".join(msg)

