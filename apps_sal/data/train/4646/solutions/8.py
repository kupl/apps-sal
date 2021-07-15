from string import ascii_lowercase as alphabet
def encode(s):
    POS={v:i%2 for i,v in enumerate(alphabet)}
    return "".join(str(POS.get(c,c)) for c in s.lower())
