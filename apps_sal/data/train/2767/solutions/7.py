import re
def is_matched(read):
    res = [int(i) for i in re.findall(r"\d+",read[0])]
    if sum(res) != len(read[1]):
        return "Invalid cigar"
    if len(res) == 1 and "M" in read[0]:
        return True
    return False
