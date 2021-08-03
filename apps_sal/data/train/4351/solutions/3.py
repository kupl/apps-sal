from functools import reduce
import re


def find_middle(string):
    try:
        nums = re.findall(r'\d', string)
        result = str(reduce(lambda x, y: x * y, (int(x) for x in nums)))
        return int(result[(len(result) - 1) // 2:len(result) // 2 + 1])
    except:
        return -1
