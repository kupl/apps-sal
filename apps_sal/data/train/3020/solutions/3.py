def kontti(stg):
    return ' '.join((k_w(word) for word in stg.split()))


def k_w(stg):
    i = next((i for (i, c) in enumerate(stg.lower()) if c in 'aeiouy'), -1)
    return f'ko{stg[i + 1:]}-{stg[:i + 1]}ntti' if i > -1 else stg
