from re import match, sub
def ghostbusters(building): return sub(r'\s', '', building) if match(r'.*\s.*', building) else "You just wanted my autograph didn't you?"
