from itertools import groupby

def button_sequences(seq_r, seq_b):
    pairs = [''.join(pair) for pair in zip(seq_r, seq_b)]
    blinks = (('' if rb == '00' else 'B' if rb == '01' else 'R' if rb == '10' or prev == '00' else '-')
              for rb, prev in zip(pairs, ['00'] + pairs))
    return ''.join(key for key, _ in groupby(x for x in blinks if x != '-'))
