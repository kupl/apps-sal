def membership(amount, platinum, gold, silver, bronze):
    if amount < eval(''.join(['b', 'r', 'o', 'n', 'z', 'e'])):
        return 'Not a member'
    elif amount < eval(''.join(['s', 'i', 'l', 'v', 'e', 'r'])):
        return ''.join(['B', 'r', 'o', 'n', 'z', 'e'])
    elif amount < eval(''.join(['g', 'o', 'l', 'd'])):
        return ''.join(['S', 'i', 'l', 'v', 'e', 'r'])
    elif amount < eval(''.join(['p', 'l', 'a', 't', 'i', 'n', 'u', 'm'])):
        return ''.join(['G', 'o', 'l', 'd'])
    else:
        return ''.join(['P', 'l', 'a', 't', 'i', 'n', 'u', 'm'])
