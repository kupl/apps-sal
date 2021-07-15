def relations(family_list, target_pair):    
    
    daughters = set()
    mothers = {}
    
    for (mother, daughter) in family_list:
        if mother in daughters: daughters.remove(mother)
        daughters.add(daughter)        
        mothers[daughter] = mother
    
    get_ancestors = lambda d : (get_ancestors(mothers[d]) if d in mothers else []) + [d]        
    
    p1, p2 = target_pair
    
    rs = {1: 'Mother', -1: 'Daughter', 2: 'Grandmother', -2: 'Granddaughter'}    
    
    for daughter in daughters:
        
        ancestors = get_ancestors(daughter)        
        if p1 in ancestors and p2 in ancestors: return rs[ancestors.index(p1) - ancestors.index(p2)]
        
    mother1 = mothers.get(p1, None)
    mother2 = mothers.get(p2, None)
    
    if mother1 and mother2 and mother1 == mother2: return 'Sister'
    
    grandmother1 = mothers.get(mother1, None)
    grandmother2 = mothers.get(mother2, None)
    
    if grandmother1 == grandmother2: return 'Cousin'
    
    return 'Aunt' if grandmother1 == mother2 else 'Niece'
