from string import ascii_lowercase
from collections import OrderedDict

def keyword_cipher(msg,keyword):
    return msg.lower().translate(str.maketrans(ascii_lowercase,''.join(OrderedDict.fromkeys(keyword.lower()+ascii_lowercase).keys())))
