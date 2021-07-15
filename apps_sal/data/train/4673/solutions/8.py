def convert_hash_to_array(hash):
    my_list = []
    for k in sorted(hash.items()):
        temp = [k[0], k[1]]
        my_list.append(temp)
    return my_list
