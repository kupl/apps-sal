def average_string(s):
    sn = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    a = 0
    try:
        for i in s.split():
            a += sn[i]
        a /= len(s.split())
    except:
        return 'n/a'
    return list(sn.keys())[list(sn.values()).index(int(a))]
