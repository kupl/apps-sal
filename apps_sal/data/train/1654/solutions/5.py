import re


def solve_runes(runes):
    m = re.match('(-?[0-9?]+)([-+*])(-?[0-9?]+)=(-?[0-9?]+)', runes)
    nums = [m.group(1), m.group(3), m.group(4)]
    op = m.group(2)
    for v in range(0, 10):
        if str(v) in runes:
            continue
        testNums = [num.replace('?', str(v)) for num in nums]
        for num in testNums:
            if re.match('(^0|^(-0))[0-9]+', num):
                break
        else:
            if int(testNums[2]) == eval(testNums[0] + op + testNums[1]):
                return v
    return -1
