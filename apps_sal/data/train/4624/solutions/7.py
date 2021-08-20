from collections import Counter


def gc_content(seq):
    c = Counter(seq)
    return round((c['C'] + c['G']) / len(seq) * 100, 2) if seq else 0
