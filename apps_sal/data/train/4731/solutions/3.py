def match(usefulness, months):
    return f"{('M' if sum(usefulness) >= 100 * 0.85 ** months else 'No m')}atch!"
