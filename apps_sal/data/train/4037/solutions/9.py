
import re


def detect_operator(num):
    s = '''    
    039 xxx xx xx - Golden Telecom
    050 xxx xx xx - MTS
    063 xxx xx xx - Life:)
    066 xxx xx xx - MTS
    067 xxx xx xx - Kyivstar
    068 xxx xx xx - Beeline
    093 xxx xx xx - Life:)
    095 xxx xx xx - MTS
    096 xxx xx xx - Kyivstar
    097 xxx xx xx - Kyivstar
    098 xxx xx xx - Kyivstar
    099 xxx xx xx - MTS Test [Just return "MTS"]
'''
    rs = re.findall('0(\d\d).+ - (.*)\n', s)
    rm = re.findall('80(\d\d)\d{7}', num)
    for i in rs:
        if rm[0] in i:
            if 'Test' in i[1]:
                return 'MTS'
            return i[1]
    return 'no info'
