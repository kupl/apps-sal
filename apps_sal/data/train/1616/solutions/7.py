from functools import reduce


def parse_int(string):
    unit_ts = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000}
    text = string.split(' ')
    lst = []
    for element in text:
        if '-' in element:
            lst.append(unit_ts[element.split('-')[0]] + unit_ts[element.split('-')[1]])
        elif element in unit_ts:
            lst.append(unit_ts[element])
    myid = lst.index(max(lst))
    result = 0
    result += reduce(lambda x, y: x * y if y % 100 == 0 else x + y, lst[:myid + 1]) if lst[:myid + 1] != [] else 0
    result += reduce(lambda x, y: x * y if y % 100 == 0 else x + y, lst[myid + 1:]) if lst[myid + 1:] != [] else 0
    return result
