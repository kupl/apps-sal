def triple_trouble(one, two, three):
    return ''.join([f'{one[x]}{two[x]}{three[x]}' for x in range(len(one))])
