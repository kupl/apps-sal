import string
from collections import Counter
def missing_alphabets(s):
    my_dict = Counter(s)
    set = max(my_dict.values())
    return "".join([letter*(set-my_dict[letter]) for letter in string.ascii_lowercase])
