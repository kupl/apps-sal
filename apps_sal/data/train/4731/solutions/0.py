def match(usefulness, months):
    return 'Match!' if sum(usefulness) >= 0.85 ** months * 100 else 'No match!'
