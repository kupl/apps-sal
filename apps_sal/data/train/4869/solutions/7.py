import json
def find_seventh_sons_of_seventh_sons(jstring,z=[]):
    if type(jstring)==str:
        jstring=json.loads(jstring)
        z=[]
    if len(jstring['children'])>6 and all(children['gender']=='male' for children in jstring['children'])and len(jstring['children'][6]['children'])>6 and all(jstring['children'][6]['children'][i]['gender']=='male' for i in range(7)):
        z.append(jstring['children'][6]['children'][6]['name'])
    for x in jstring['children']:
        find_seventh_sons_of_seventh_sons(x,z)
    return set(z)
