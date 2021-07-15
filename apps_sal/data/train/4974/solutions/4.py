def user_contacts(data):
    dictionary={}
    for t in data:
        if len(t)==1:
            dictionary[t[0]]=None
        elif len(t)==2:
            dictionary[t[0]]=t[1]
    return dictionary
