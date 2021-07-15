def self_converge(number, seen=None):
    number = str(number)
    digits = ''.join(sorted(number))
    result = '{{:0{}}}'.format(len(number)).format(int(digits[::-1]) - int(digits))
    if int(result) == 0:
        return -1
    elif seen and result in seen:
        return len(seen) + 1
    else:
        return self_converge(result, (seen or []) + [result])
