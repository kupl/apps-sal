def relations(family_list, target_pair):
    for i in family_list:
        if target_pair[0] == i[1]:
            for j in family_list:
                if target_pair[1] == j[1] and j[0] == i[0]:
                    return 'Sister'
        if i == target_pair:
            return("Daughter")
        elif i[0] == target_pair[1] and i[1] == target_pair[0]:
            return("Mother")
        elif target_pair[0] == i[1]:
            for j in family_list:
                if i[0] == j[1] and target_pair[1] == j[0]:
                    return 'Grandmother'
        elif target_pair[1] == i[1]:
            for j in family_list:
                if i[0] == j[1] and target_pair[0] == j[0]:
                    return 'Granddaughter'
        if target_pair[0] == i[1]:
            gmm = 1
            for j in family_list:
                if i[0] == j[1]:
                    gmm = j[0]
            for k in family_list:
                if target_pair[1] == k[1]:
                    for m in family_list:
                        if k[0] == m[1] and m[0] == gmm:
                            return 'Cousin'
        if target_pair[0] == i[1]:
            for j in family_list:
                if j[1] == i[0]:
                    for k in family_list:
                        if k[0] == j[0] and k != j and target_pair[1] == k[1]:
                            return 'Aunt'
        if target_pair[1] == i[1]:
            for j in family_list:
                if j[1] == i[0]:
                    for k in family_list:
                        if k[0] == j[0] and k != j and target_pair[0] == k[1]:
                            return 'Niece'
