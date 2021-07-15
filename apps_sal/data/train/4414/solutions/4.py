import itertools

def compare_versions(v1,v2):
    p = list(map(int, v1.split('.')))
    q = list(map(int, v2.split('.')))
    for i, v in itertools.zip_longest(p, q, fillvalue=0):
        if i < v:
            return False
    return True
