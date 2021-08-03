from string import digits, ascii_uppercase as auc


def play_pass(s, n):
    return ''.join(a.lower() if c % 2 else a for c, a in enumerate(s.translate(str.maketrans(auc + digits, auc[n:] + auc[:n] + digits[::-1]))))[::-1]
