from re import findall, IGNORECASE


def trump_detector(trump_speech):
    final = [len(c[1]) for c in findall('([aeiou])(\\1*)', trump_speech, IGNORECASE)]
    return round(sum(final) / len(final), 2)
