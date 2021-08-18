import re

INVALID_WORDS = set("the of in from by with and or for to at a".upper().split())


def formater(part):
    part = part.replace("-", " ").upper()
    if len(part) > 30:
        part = ''.join(w[0] for w in part.split() if w not in INVALID_WORDS)
    return part


def generate_bc(url, separator):
    ans, urlLst = [], re.sub(r'( / index\..*)|(\?.*)|(
    lenLst=len(urlLst)

    for i in range(lenLst):
        if i == 0 and lenLst > 1:
            ans.append('<a href="/">HOME</a>')
        elif i != lenLst - 1 and len(urlLst) > 2:
            ans.append('<a href="/{}/">{}</a>'.format('/'.join(urlLst[1:i + 1]), formater(urlLst[i])))
        elif i == lenLst - 1:
            ans.append('<span class="active">{}</span>'.format('HOME' if i == 0 else formater(re.sub(r'\..*', '', urlLst[-1]))))

    return separator.join(ans)
