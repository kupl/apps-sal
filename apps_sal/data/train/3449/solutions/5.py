def categorize_study(p, r):
    cat = p * 2 ** (6 - r)
    return 'Fine' if cat < 0.05 and r else 'Needs review' if cat < 0.15 else 'Pants on fire'
