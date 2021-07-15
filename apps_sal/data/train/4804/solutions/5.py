def relations(family_list, target_pair):
    for i in family_list:
        if target_pair[0] == i[1]:
            for j in family_list:
                if target_pair[1] == j[1] and j[0]==i[0]:
                    return 'Sister'
        if i==target_pair:
            return("Daughter")
        elif i[0]==target_pair[1] and i[1]==target_pair[0]:
            return("Mother")
        elif target_pair[0]==i[1]:
            for j in family_list:
                if i[0]==j[1] and target_pair[1] == j[0]:
                    return 'Grandmother'
        elif target_pair[1]==i[1]:
            for j in family_list:
                if i[0]==j[1] and target_pair[0] == j[0]:
                    return 'Granddaughter'
        if target_pair[0]==i[1]:
            Gmm=1
            for j in family_list:
                if i[0]==j[1]:
                    Gmm=j[0]
            for k in family_list:
                if target_pair[1]==k[1]:
                    for m in family_list:
                        if k[0]==m[1] and m[0]==Gmm:
                            return("Cousin")
        if target_pair[0]==i[1]:
            for j in family_list:
                if j[1]==i[0]:
                    for k in family_list:
                        if k[0]==j[0] and k[1]==target_pair[1] and k!=j:
                            return ("Aunt")
        if target_pair[1]==i[1]:
            for j in family_list:
                if j[1]==i[0]:
                    for k in family_list:
                        if k[0]==j[0] and k[1]==target_pair[0] and k!=j:
                            return ("Niece")
                            
        
                    

print((relations([('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')],("Dianne","Deborah"))))

