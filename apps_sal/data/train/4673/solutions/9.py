def convert_hash_to_array(hash):
    return sorted([[att, hash[att]] for att in hash])
