def match(usefulness, months):
    return ["Match!", "No match!"][sum(usefulness) < 100 * 0.85 ** months]
