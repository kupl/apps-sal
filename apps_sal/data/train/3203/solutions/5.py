from collections import Counter
import re

def parse_mana_cost(s):
    s = s.lower()
    if re.match(r"\d*[wubrg]*\Z", s):
        r = {x: s.count(x) for x in set(s) if x.isalpha()}
        return s and s[0].isdigit() and int(s[0]) and r.update({"*": int(re.match(r"\d+", s).group())}) or r
