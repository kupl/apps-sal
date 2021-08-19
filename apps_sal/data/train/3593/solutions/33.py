def capitalize(s, ind):
    return ''.join((s[x] if x not in ind else s[x].upper() for x in range(len(s))))
