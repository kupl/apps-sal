def ordered(l, arr1,arr2):
    return [l,arr2.index(l) + len(arr1) if l in arr2 else arr1.index(l)]

def hot_singles(arr1, arr2):
    L = [ ordered(l,arr1,arr2) for l in set(arr1) ^ set(arr2)]
    return list(map(lambda l: l[0], sorted(L , key=lambda l: l[1])))
