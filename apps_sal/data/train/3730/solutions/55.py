def capitalize(s):
    final1 = ""
    final2 = ""

    for x in range(len(s)):
        final1 += s[x].upper() if x % 2 == 0 else s[x]

    for x in final1:
        final2 += x.lower() if x.isupper() else x.upper()

    return [final1, final2]
