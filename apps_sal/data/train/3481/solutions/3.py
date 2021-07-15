from collections import Counter
def get_char_count(s):
    con = Counter([e for e in s.lower() if any((e.isalpha(), e.isdigit()))])
    return { v:sorted([e for e in con.keys() if con[e] == v]) for v in sorted(con.values(), reverse = 1 ) }
