import re

def is_matched(read):
    nums = [int(v) for v in re.findall(r'\d+', read[0])]
    return 'Invalid cigar' if sum(nums)!=len(read[1]) else read[0]==f'{len(read[1])}M'
