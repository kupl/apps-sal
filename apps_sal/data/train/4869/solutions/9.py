def find_seventh_sons_of_seventh_sons(family_dict, ss_set=set()):
    """
    List of seven sons of seventh son is checked if any girl is born in between.
    """
    if type(family_dict) == str:
        ss_set.clear()
        family_dict = json.loads(family_dict)
    if len(family_dict['children']) > 6 and len(family_dict['children'][6]['children']) > 6:
        children_genders = [x['gender'] for x in family_dict['children'][:7]] + [x['gender'] for x in family_dict['children'][6]['children'][:7]]
        if not 'female' in children_genders:
            ss_set.add(family_dict['children'][6]['children'][6]['name'])
    for child in family_dict['children']:
        find_seventh_sons_of_seventh_sons(child, ss_set)
    return ss_set
