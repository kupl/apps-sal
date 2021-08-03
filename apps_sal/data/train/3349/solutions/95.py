def find_missing_number(sequence):
    if sequence == '':
        return 0
    elif not all([x.isdigit() for x in sequence.split()]):
        return 1
    else:
        s = sorted(sequence.split(), key=lambda x: int(x))
        print((int(s[0])))
        for x in range(len(s) - 1):
            if int(s[x + 1]) - int(s[x]) != 1:
                return int(s[x]) + 1
            elif int(s[0]) != 1:
                return 1
            elif len(s) == int(s[-1]):
                return 0
