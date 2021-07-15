import re

def is_matched(read):
    cigar, seq = read
    matches = re.findall(r'(\d+)([A-Z])', cigar)
    if sum(int(n) for n, _ in matches) != len(seq):
        return 'Invalid cigar'
    return all(sym == 'M' for _, sym in matches)
