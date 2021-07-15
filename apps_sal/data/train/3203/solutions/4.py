import re
from collections import Counter


def parse_mana_cost(mana):
    for cnt, chrs in re.findall(r"\A(\d*)([wubrg]*)\Z", mana.lower() or "0"):
        result = {"*": int(cnt or 0), **Counter(chrs)}
        return {key: result[key] for key in result if result[key]}
