import re


def siegfried(week, txt):
    lessons = [[('c(?=[ie])', {'c': 's', 'C': 'S'}), ('c(?!h)', {'c': 'k', 'C': 'K'})], [('ph', {'ph': 'f', 'Ph': 'F'})], [('(?<=\\w\\w\\w)e(?=\\W|\\Z)', {'e': '', 'E': ''}), ('([a-z])\\1', {})], [('th', {'th': 'z', 'Th': 'Z'}), ('wr', {'wr': 'r', 'Wr': 'R'}), ('wh', {'wh': 'v', 'Wh': 'V'}), ('w', {'w': 'v', 'W': 'V'})], [('ou', {'ou': 'u', 'Ou': 'U'}), ('an', {'an': 'un', 'An': 'Un'}), ('ing(?=\\W|\\Z)', {'ing': 'ink'}), ('(?<=\\W)sm|(?<=\\A)sm', {'sm': 'schm', 'Sm': 'Schm'})]]
    result = txt
    for w in range(week):
        for (rx, data) in lessons[w]:

            def repl(m):
                return data.get(m.group(0), m.group(0)[0])
            result = re.sub(rx, repl, result, flags=re.IGNORECASE)
    return result
