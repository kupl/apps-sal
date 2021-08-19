def vowel_shift(text, n):
    if text in (None, ''):
        return text
    vwl = [x for x in text if x in 'aeiouAEIOU']
    if len(vwl) == 0:
        return text
    n %= len(vwl)
    vwl = list(vwl[-n:] + vwl[:-n])
    return ''.join([x if x not in 'aeiouAEIOU' else vwl.pop(0) for x in text])
