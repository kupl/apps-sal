def str_count(strng, letter):
    import re
    list = re.findall(letter, strng)
    return len(list)

