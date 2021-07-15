import string
def keyword_cipher(msg, keyword):
    s = []
    for i in keyword.lower():
        if i not in s:
            s.append(i)
    return msg.lower().translate(str.maketrans(string.ascii_lowercase, ''.join(s + [i for i in string.ascii_lowercase if i not in keyword]).lower()))
