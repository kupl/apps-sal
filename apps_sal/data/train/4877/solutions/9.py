from itertools import cycle
import operator


def love_language(partner, weeks):
    counts = {}
    for l in LOVE_LANGUAGES:
        counts[l] = 0
    for (lang, week) in zip(cycle(LOVE_LANGUAGES), range(weeks * 7)):
        counts[lang] += int(partner.response(lang) == 'positive')
    return max(counts.items(), key=operator.itemgetter(1))[0]
