def relations(family_list, target_pair):
    def code(family_list, target_pair):
        source,target = target_pair
        for rel in family_list:
            for i in (0,1):
                if rel[i] == source:
                    if rel[1-i] == target: return 'cp'[i]
                    branch = code(family_list - set([rel]), (rel[1-i], target))
                    if branch: return 'cp'[i] + branch
    m = {
        'p':'Mother','pp':'Grandmother',
        'c':'Daughter','cc':'Granddaughter',
        'pc':'Sister','pcc':'Niece',
        'ppc':'Aunt','ppcc':'Cousin'
    }
    return m[code(set(family_list), target_pair)]
