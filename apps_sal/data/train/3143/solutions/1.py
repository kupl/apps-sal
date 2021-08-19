S = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENTH = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def convertToString(n):
    if not n:
        return 'zero'
    (c, t, u) = map(lambda v: n % (v * 10) // v, (100, 10, 1))
    return ' '.join((s for s in ['{} hundred'.format(S[c]) * bool(c), TENTH[t], S[u + 10 * (t == 1)]] if s))


def sort_by_name(arr):
    return sorted(arr, key=convertToString)
