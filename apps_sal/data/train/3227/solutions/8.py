def to_lover_case(string):
    dic = {0: 'L', 1: 'O', 2: 'V', 3: 'E'}
    return "".join([dic[((ord(i.lower()) - 97) % 4)] if i.isalpha() else i for i in string])
