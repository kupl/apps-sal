def digitize(num):
    if len(str(num)) == 1:
        return num
    output = []
    for n in reversed(str(num)):
        output.append(int(n))
    return output
