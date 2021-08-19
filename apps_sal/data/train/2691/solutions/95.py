def solve(s):
    s += '.'
    arr = []
    num = ''
    for i in s:
        if i.isnumeric():
            num += i
        else:
            if num != '':
                arr.append(int(num))
            num = ''
    arr.sort()
    return arr[-1]
