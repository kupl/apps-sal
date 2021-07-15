from string import ascii_lowercase
id = {c:i for i,c in enumerate(ascii_lowercase)}
char = (ascii_lowercase+ascii_lowercase).__getitem__

def hamster_me(code, message):
    res, L = {}, sorted(map(id.get, code))
    for i,j in zip(L, L[1:]+[26+L[0]]):
        start = char(i)
        for k,x in enumerate(map(char, range(i, j)), 1):
            res[x] = f"{start}{k}"
    return ''.join(map(res.get, message))
