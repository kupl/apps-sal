def relations(family_list, target_pair):
    tree = {}
    for parent, child in family_list:
        tree[child] = parent

    a = tree.get(target_pair[0], 0)
    b = tree.get(target_pair[1], 0)
    if a == b:
        return 'Sister'
    elif a == target_pair[1]:
        return 'Mother'
    elif b == target_pair[0]:
        return 'Daughter'

    cnt_a = 0
    while a and a != target_pair[1]:
        cnt_a += 1
        a = tree.get(a, 0)

    cnt_b = 0
    while b and b != target_pair[0]:
        cnt_b += 1
        b = tree.get(b, 0)

    if a and not b and cnt_a == 1:
        return 'Grandmother'
    elif not a and not b and cnt_a == cnt_b:
        return 'Cousin'
    elif not a and not b and cnt_a < cnt_b:
        return 'Niece'
    elif not a and not b and cnt_a > cnt_b:
        return 'Aunt'
    elif not a and cnt_b == 1:
        return 'Granddaughter'
    else:
        return None
