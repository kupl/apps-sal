def generate_hashtag(s):
    if 140 > len(s) > 0:
        L = s.split(' ')
        L1 = []
        for i in L:
            L1.append(i.capitalize())
        return '#' + str(''.join(L1))
    else:
        return False
