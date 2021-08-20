def number(lines):
    res = []
    count = 0
    for item in lines:
        st = str(count + 1) + ': ' + item
        count += 1
        res.append(st)
    return res
