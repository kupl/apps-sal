def ranking(people):
    S = sorted((d['points'] for d in people))[::-1]
    return [{**d, **{'position': S.index(d['points']) + 1}} for d in sorted(people, key=lambda k: (-k['points'], k['name']))]
