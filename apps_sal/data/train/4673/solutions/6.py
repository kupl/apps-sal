def convert_hash_to_array(hash):
    dictlist = []
    for key, value in hash.items():
        temp = [key,value]
        dictlist.append(temp)
    return sorted(dictlist)
