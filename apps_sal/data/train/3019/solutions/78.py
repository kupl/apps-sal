import re
def str_count(strng, letter):
    x = re.findall(letter, strng)
    return len(x)
