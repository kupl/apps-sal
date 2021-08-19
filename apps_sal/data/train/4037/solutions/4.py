import re


def detect_operator(num):
    d = {'0(66|50|9[59])': 'MTS', '0[69]3': 'Life:)', '0(9[6-8]|67)': 'Kyivstar', '068': 'Beeline', '039': 'Golden Telecom'}
    for temp in d:
        if re.fullmatch(temp, num[1:4]):
            return d[temp]
    return 'no info'
