from collections import Counter


def love_language(partner, weeks):
    c = Counter()
    for i in range(7 * weeks // 5):
        for lang in ['words', 'acts', 'gifts', 'time', 'touch']:
            if partner.response(lang) == 'positive':
                c[lang] += 1
    return max(c, key=c.get)
