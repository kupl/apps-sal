def tongues(code):
    map1 = 'aiyeoubkxznhdcwgpvjqtsrlmf'
    map2 = 'eouaiypvjqtsrlmfbkxznhdcwg'
    return code.translate(str.maketrans(map1+map1.upper(), map2+map2.upper()))
