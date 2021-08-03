import re


def pete_talk(s, ok=[]):
    ok = list(map(lambda x: x.lower(), ok))
    return re.sub(r'((?<=^)|(?<=[?.!] ))\w', lambda x: x.group(0).upper(), ' '.join([(i[0] + '*' * (len(i) - 2 - int(i[-1] in '!.,?;:')) + i[-[1, 2][i[-1] in '!.,;?:']:])if[i, i[:-1]][i[-1] in '!.,;?:']not in ok and len(i) > 2else i for i in s.lower().split()]))
