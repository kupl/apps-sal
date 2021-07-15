def convert_hash_to_array(hash):
    return [[k, hash[k]] for k in sorted(hash)]
