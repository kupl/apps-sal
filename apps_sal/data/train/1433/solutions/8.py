
t = int(input())

# adict = [0]*10;
# bdict = [0]*10;

for i in range(0, t):
    a = input()
    b = input()

    # lena = len(a);

    agts = bgts = afour = bfour = aseven = bseven = altf = bltf = afts = bfts = 0

    for j in a:
        if j > '7':
            agts = agts + 1
        elif j == '7':
            aseven = aseven + 1
        elif j > '4':
            afts = afts + 1
        elif j == '4':
            afour = afour + 1
        else:
            altf = altf + 1

    for j in b:
        if j > '7':
            bgts = bgts + 1
        elif j == '7':
            bseven = bseven + 1
        elif j > '4':
            bfts = bfts + 1
        elif j == '4':
            bfour = bfour + 1
        else:
            bltf = bltf + 1

    # for j in range(0,10):
        # adict[j] = 0;
        # bdict[j] = 0;

    # for j in range(0,lena):
        # adict[int(a[j])] = adict[int(a[j])] + 1
        # bdict[int(b[j])] = bdict[int(b[j])] + 1

    # agts = adict[8] + adict[9]
    # bgts = bdict[8] + bdict[9]

    # aseven = adict[7]
    # bseven = bdict[7]

    # afts = adict[5] + adict[6]
    # bfts = bdict[5] + bdict[6]

    # afour = adict[4]
    # bfour = bdict[4]

    # altf = adict[0] + adict[1] + adict[2] + adict[3]
    # bltf = bdict[0] + bdict[1] + bdict[2] + bdict[3]

    nseven = 0
    nfour = 0

    if aseven > bfts:
        aseven = aseven - bfts
        nseven = nseven + bfts
        bfts = 0
    else:
        bfts = bfts - aseven
        nseven = nseven + aseven
        aseven = 0

    if bseven > afts:
        bseven = bseven - afts
        nseven = nseven + afts
        afts = 0
    else:
        afts = afts - bseven
        nseven = nseven + bseven
        bseven = 0

    if aseven > bltf:
        aseven = aseven - bltf
        nseven = nseven + bltf
        bltf = 0
    else:
        bltf = bltf - aseven
        nseven = nseven + aseven
        aseven = 0

    if bseven > altf:
        bseven = bseven - altf
        nseven = nseven + altf
        altf = 0
    else:
        altf = altf - bseven
        nseven = nseven + bseven
        bseven = 0

    if aseven > bfour:
        aseven = aseven - bfour
        nseven = nseven + bfour
        bfour = 0
    else:
        bfour = bfour - aseven
        nseven = nseven + aseven
        aseven = 0

    if bseven > afour:
        bseven = bseven - afour
        nseven = nseven + afour
        afour = 0
    else:
        afour = afour - bseven
        nseven = nseven + bseven
        bseven = 0

    nseven = nseven + min(aseven, bseven)

    if afour > bltf:
        afour = afour - bltf
        nfour = nfour + bltf
        bltf = 0
    else:
        bltf = bltf - afour
        nfour = nfour + afour
        afour = 0

    if bfour > altf:
        bfour = bfour - altf
        nfour = nfour + altf
        altf = 0
    else:
        altf = altf - bfour
        nfour = nfour + bfour
        bfour = 0

    nfour = nfour + min(afour, bfour)

    if nseven + nfour > 0:
        print('7' * nseven + '4' * nfour)
    else:
        print()
