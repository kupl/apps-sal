def siegfried(week, txt):

    import re

    dict_week = \
        {
            1: {'Ci': 'Si', 'Ce': 'Se', 'Ch': 'Xxx', 'C': 'K', 'Xxx': 'Ch',
                'ci': 'si', 'ce': 'se', 'ch': 'xxx', 'c': 'k', 'xxx': 'ch'},
            2: {'Ph': 'F', 'ph': 'f'},
            3: {'': ''},
            4: {'Th': 'Z', 'Wr': 'R', 'Wh': 'V', 'W': 'V',
                'th': 'z', 'wr': 'r', 'wh': 'v', 'w': 'v'},
            5: {'Ou': 'U', 'An': 'Un', 'ou': 'u', 'an': 'un'}
        }

    dd = {}
    for i in range(1, week + 1):
        dd.update(dict_week[i])

    for k, v in dd.items():
        txt = txt.replace(k, v)

    if week >= 3:
        txt = ''.join(re.sub(r'e$', '', i) if len(i) > 3 else i for i in re.split(r'(\W)', txt))
        double_l = {re.search(r'([a-z])\1', i).group(0) for i in txt.lower().split() if re.search(r'([a-z])\1', i)}
        for i in double_l:
            txt = txt.replace(i, i[0])
            txt = txt.replace(i[0].upper() + i[1], i[0].upper())

    if week == 5:
        txt = ' '.join(re.sub(r'ing$', 'ink', i, flags=re.IGNORECASE) for i in txt.split())
        txt = ' '.join(re.sub(r'^sm', 'Schm', i, flags=re.IGNORECASE) for i in txt.split())

    return txt
