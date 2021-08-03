import re
import operator


def calculate(s):
    match_res = re.match(r'.+\s(\d+)\s.+\s(loses|gains)\s(\d+)\Z', s.strip())
    try:
        return {
            'loses': operator.sub,
            'gains': operator.add,
        }[match_res.group(2)](int(match_res.group(1)), int(match_res.group(3)))
    except AttributeError:
        raise ValueError('string do not obey sepcific')
