import re


def siegfried(week, txt):
    lessons = \
        [
            [
                (r'c(?=[ie])', {'c': 's', 'C': 'S'}),
                (r'c(?!h)', {'c': 'k', 'C': 'K'})
            ], [
                (r'ph', {'ph': 'f', 'Ph': 'F'})
            ], [
                (r'(?<=\w\w\w)e(?=\W|\Z)', {'e': '', 'E': ''}),
                (r'([a-z])\1', {})
            ], [
                (r'th', {'th': 'z', 'Th': 'Z'}),
                (r'wr', {'wr': 'r', 'Wr': 'R'}),
                (r'wh', {'wh': 'v', 'Wh': 'V'}),
                (r'w', {'w': 'v', 'W': 'V'})
            ], [
                (r'ou', {'ou': 'u', 'Ou': 'U'}),
                (r'an', {'an': 'un', 'An': 'Un'}),
                (r'ing(?=\W|\Z)', {'ing': 'ink'}),
                (r'(?<=\W)sm|(?<=\A)sm', {'sm': 'schm', 'Sm': 'Schm'})
            ]
        ]

    result = txt
    for w in range(week):
        for rx, data in lessons[w]:
            def repl(m): return data.get(m.group(0), m.group(0)[0])
            result = re.sub(rx, repl, result, flags=re.IGNORECASE)
    return result
