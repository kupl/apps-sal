import re


def insert_dash2(num):
    return re.sub('[13579](?=[13579])|[2468](?=[2468])', lambda m: m.group(0) + ('-' if int(m.group(0)) & 1 else '*'), str(num))
