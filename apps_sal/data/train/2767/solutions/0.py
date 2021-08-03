import re


def is_matched(read):
    total = sum([int(num) for num in re.findall(r'\d+', read[0])])

    if read[0] == str(len(read[1])) + 'M':
        return True
    elif len(read[1]) != total:
        return 'Invalid cigar'
    else:
        return False
