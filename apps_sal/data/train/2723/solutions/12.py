def average_string(s):
    try:
        l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        s = s.split(' ')
        c = 0
        for i in s:
            c += l.index(i)
        c = int(c / len(s))
        return l[c]
    except:
        return "n/a"
