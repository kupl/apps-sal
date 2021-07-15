import re


def cycle(sequence):
    string = ' ' + ' '.join(str(n) for n in sequence)
    pattern = re.compile(r'([\d ]+)(\1)')
    matches = pattern.search(string)
    
    if matches is None:
        return []
        
    seq = matches.group(1)
    sequence = seq.strip().split()
    not_in = int(string.replace(seq, '') or 0)
    return [not_in, 1 if len(set(sequence)) == 1 else len(sequence)]
