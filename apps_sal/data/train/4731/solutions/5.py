def match(usefulness, months):
    match = sum(usefulness) >= 100 * 0.85 ** months
    return 'Match!' if match else 'No match!'
