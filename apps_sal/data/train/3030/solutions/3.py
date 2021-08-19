def nb_dig(n, d):

    tot_occur = 0

    for i in range(n + 1):
        # print(i**2)
        tot_occur += str(i**2).count(str(d))

    return tot_occur
