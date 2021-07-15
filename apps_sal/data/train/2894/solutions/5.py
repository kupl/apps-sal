def triple_trouble(one, two, three):
    return ''.join([one[i] + two[i] + three[i] for i in range(len(one))])
