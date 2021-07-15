from string import ascii_lowercase

def keyword_cipher(msg, keyword):
    key = list(dict.fromkeys(keyword + ascii_lowercase).keys())
    return ''.join(key[ascii_lowercase.index(c)] if c in key else c for c in msg.lower())

