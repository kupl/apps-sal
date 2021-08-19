def convert_to_mixed_numeral(parm):
    # your code here
    parts = tuple(map(int, parm.split('/')))
    a, b = abs(parts[0]), parts[1]
    if a < b:
        mixed_numeral = "{}/{}".format(a, b)
    elif a % b:
        mixed_numeral = "{} {}/{}".format(a // b, a % b, b)
    else:
        mixed_numeral = str(a // b)
    if parts[0] < 0:
        mixed_numeral = "-{}".format(mixed_numeral)

    return mixed_numeral  # mixed_numeral is a string
