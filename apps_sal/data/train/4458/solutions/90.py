def time_correct(t: str):
    returnlst = []
    add = 0
    number = 0
    if t == '':
        return ''
    if t == None or len(t.split(':')) != 3:
        return None

    for ind, val in [(ind, val) for ind, val in enumerate(t.split(':')[::-1])]:
        try:
            if any(ops in val for ops in ['+', '-', '/', '\\', '*', '=']):
                return None
            if len(val) == 2:
                number = int(val)
            else:
                return None
        except ValueError:
            return None
        if ind == 2:
            number += add
            returnlst.append(str(number % 24).zfill(2))
        else:
            number += add
            add = int(number / 60)
            returnlst.append(str(number % 60).zfill(2))
    return ':'.join(returnlst[::-1])
