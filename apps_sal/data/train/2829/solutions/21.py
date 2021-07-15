def array_madness(a,b):
    resa = 0
    resb = 0
    for num in a:
        resa += num**2
    for num in b:
        resb += num**3
    return resa > resb
