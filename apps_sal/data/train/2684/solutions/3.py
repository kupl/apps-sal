UNITS = " jeden dwa trzy cztery piec szesc siedem osiem dziewiec".split(" ")
TENS = "dziesiec jedenascie dwanascie trzynascie czternascie pietnascie szesnascie siedemnascie osiemnascie dziewietnascie".split(" ")
TENTH = "  dwadziescia trzydziesci czterdziesci piecdziesiat szescdziesiat siedemdziesiat osiemdziesiat dziewiecdziesiat".split(" ")

def ordering_beers(n):
    if not 0 <= n < 100: raise ValueError("Nie wiem")
    t, u = divmod(n, 10)
    number = {0: UNITS[u], 1: TENS[u]}.get(t, TENTH[t] + " " * (u > 0) + UNITS[u])
    plural = "piwa" if t != 1 and 1 < u < 5 else "piw"
    order = {0: "woda mineralna", 1: "jedno piwo"}.get(n, number + " " + plural)
    return "{} poprosze".format(order).capitalize()
