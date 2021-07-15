def mix(s1, s2):
    s1 = {elem: '1:' + ''.join([x for x in s1 if x == elem]) for elem in s1 if s1.count(elem) > 1 and elem.islower()}
    s2 = {elem: '2:' + ''.join([x for x in s2 if x == elem]) for elem in s2 if s2.count(elem) > 1 and elem.islower()}
    for elem in s2:
        if elem in s1:
            if len(s2.get(elem)) > len(s1.get(elem)):
                s1.update({elem: s2.get(elem)})
            elif len(s2.get(elem)) == len(s1.get(elem)):
                s1.update({elem: '=:' + s2.get(elem)[2:]})
        else:
            s1.update({elem: s2.get(elem)})
    s2 = sorted([s1.get(elem) for elem in s1])
    print(s2)
    for i in range(len(s2)):
        for j in range(len(s2)):
            if len(s2[i]) < len(s2[j]):
                s2[i], s2[j] = s2[j], s2[i]
            elif len(s2[i]) == len(s2[j]):
                if s2[i][0] == s2[j][0] and sorted([s2[i][2], s2[j][2]])[0] == s2[j][2] or \
                   s2[i][0].isdigit() == False and s2[j][0].isdigit() or \
                   s2[i][0].isdigit() and s2[j][0].isdigit() and int(s2[i][0]) > int(s2[j][0]):
                    s2[i], s2[j] = s2[j], s2[i]
    return '/'.join(reversed([x for x in s2]))
