def find_seventh_sons_of_seventh_sons(jstring):
    seventh_of_seventh = set()

    def find_seventh_sons(father, seventh_son=False):
        seven_brother = True
        for i, son in enumerate(father['children'], 1):
            if son['gender'] == 'female':
                seventh_son = seven_brother = False
            if i == 7 and seventh_son:
                seventh_of_seventh.add(son['name'])
            find_seventh_sons(son, i == 7 and seven_brother)
    find_seventh_sons(json.loads(jstring))
    return seventh_of_seventh
