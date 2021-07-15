import re
def is_matched(read):
    if f'{len(read[1])}M' == read[0]:
        return True
    elif sum(int(n) for n in re.findall('\d+', read[0])) != len(read[1]):
        return 'Invalid cigar'
    
    return False
