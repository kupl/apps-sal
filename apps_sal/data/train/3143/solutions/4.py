S = " one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")
TENTH = "  twenty thirty forty fifty sixty seventy eighty ninety".split(" ")        # Empty strings wanted at the beginning, when splitting!


def convertToString(n):
    if not n:
        return "zero"
    c, t, u = map(int, f'{n:0>3}')
    return " ".join(s for s in [f'{S[c]} hundred' * bool(c), TENTH[t], S[u + 10 * (t == 1)]] if s)


def sort_by_name(arr): return sorted(arr, key=convertToString)
