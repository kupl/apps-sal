# From slowest to fastest.

def convert_hash_to_array(hash):
    return sorted(map(list, hash.items()))


def convert_hash_to_array(hash):
    return sorted([k, v] for k, v in hash.items())


def convert_hash_to_array(hash):
    return [[k, hash[k]] for k in sorted(hash)]
