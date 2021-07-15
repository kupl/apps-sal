def triple_trouble(one, two, three):
    return ''.join(f'{one[i]}{two[i]}{three[i]}' for i in range(0,len(one)))
