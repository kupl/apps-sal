import re

def parse_mana_cost(mana):
    m = re.match(r"(\d*)([wubrg]*)\Z", mana.lower())
    if m is None:
        return
    g, c = m.groups()
    result = {} if g in ("", "0") else {"*": int(g)}
    result.update({k: c.count(k) for k in set(c)})
    return result
