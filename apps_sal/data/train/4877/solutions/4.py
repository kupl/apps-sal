def love_language(partner, weeks):
    d = {'words': 0, 'acts': 0, 'gifts': 0, 'time': 0, 'touch': 0}
    for w in range(weeks):
        for k in d.keys():
            if partner.response(k) == 'positive':
                d[k] += 1
    return max(d, key=d.get)
