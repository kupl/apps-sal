import re


def is_matched(read):
    num = re.compile(r'\d+')
    a = list(map(int, num.findall(read[0])))
    Dna_length = sum(a[0:len(a)])
    if Dna_length != len(read[1]):
        return "Invalid cigar"
    else:
        return a[0] == len(read[1]) and str(a[0]) + "M" == read[0]
