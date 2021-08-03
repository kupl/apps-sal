def match(usefulness, months):
    return 'Match!' if sum(usefulness) >= 100 * 0.85**months else 'No match!'
