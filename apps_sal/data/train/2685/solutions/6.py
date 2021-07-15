from string import ascii_lowercase

def keyword_cipher(msg, keyword):
    msg = msg.lower()
    keyword = keyword.lower()
    subs = ''.join(dict.fromkeys(keyword)) + ''.join(c for c in ascii_lowercase if c not in keyword)
    tbl = str.maketrans(ascii_lowercase, subs)
    return msg.translate(tbl)
