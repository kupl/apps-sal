def relations(family_list, target_pair):
    people = set()
    gen1 = []
    gen2 = []
    for i in family_list:
        people.add(i[0])
        people.add(i[1])
    for i in people:
        if all((j[1] != i for j in family_list)):
            gen1.append(i)
    for i in family_list:
        if i[0] in gen1:
            gen2.append(i[1])
    gen3 = [[] for i in range(len(gen2))]
    for i in family_list:
        if i[0] in gen2:
            gen3[gen2.index(i[0])].append(i[1])
    g3 = sum(gen3, [])
    (a, b) = target_pair
    if a in gen1 and b in gen2:
        return 'Daughter'
    if a in gen2 and b in gen1:
        return 'Mother'
    if a in gen1 and b in g3:
        return 'Granddaughter'
    if a in g3 and b in gen1:
        return 'Grandmother'
    if a in gen2 and b in gen2:
        return 'Sister'
    for i in gen3:
        if a in i and b in i:
            return 'Sister'
    if a in g3 and b in g3:
        return 'Cousin'
    if a in gen2 and b in gen3[gen2.index(a)]:
        return 'Daughter'
    if b in gen2 and a in gen3[gen2.index(b)]:
        return 'Mother'
    if a in gen2:
        return 'Niece'
    return 'Aunt'
