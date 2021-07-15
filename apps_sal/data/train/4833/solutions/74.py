def replace_exclamation(s):
    j="aeiouAEIOU"
    lst=['!' if x in j else x for x in s]
    return "".join(lst)
