def create_permutations(string):
    if '*' not in string:
        return [int(string)]
    return [x for i in range(10) for x in create_permutations(string.replace('*', str(i), 1))]
    

def is_divisible_by_6(string):
    return list(map(lambda x: str(x).zfill(len(string)), filter(lambda x: not x%6, create_permutations(string))))
