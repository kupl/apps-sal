def triple_trouble(one, two, three):
    return ''.join((one[n] + two[n] + three[n] for n in range(len(one))))
