import re


def is_matched(read):
    cigar = [int(i) for i in list(filter(None, re.split("[A-Z]", read[0])))]
    if(sum(cigar) == len(read[1])):
        return (len(cigar) == 1 and re.split("[0-9]+", read[0])[1] == "M")
    else:
        return 'Invalid cigar'
