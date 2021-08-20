import re


def detect_operator(num):
    s = '    \n    039 xxx xx xx - Golden Telecom\n    050 xxx xx xx - MTS\n    063 xxx xx xx - Life:)\n    066 xxx xx xx - MTS\n    067 xxx xx xx - Kyivstar\n    068 xxx xx xx - Beeline\n    093 xxx xx xx - Life:)\n    095 xxx xx xx - MTS\n    096 xxx xx xx - Kyivstar\n    097 xxx xx xx - Kyivstar\n    098 xxx xx xx - Kyivstar\n    099 xxx xx xx - MTS Test [Just return "MTS"]\n'
    rs = re.findall('0(\\d\\d).+ - (.*)\n', s)
    rm = re.findall('80(\\d\\d)\\d{7}', num)
    for i in rs:
        if rm[0] in i:
            if 'Test' in i[1]:
                return 'MTS'
            return i[1]
    return 'no info'
