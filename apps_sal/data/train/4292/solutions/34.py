def string_clean(s):
    ls = []
    final = []
    for i in s:
        if "0" <= i <= "9":
            ls.append(i)
        else:
            final.append(i)
    return ''.join(final)
