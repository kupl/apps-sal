import numpy


def primesto(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n // 2, dtype=numpy.bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return [2] + list(2 * numpy.nonzero(sieve)[0][1:] + 1)


def cum_sum_500k():
    return numpy.array([0] + primesto(500000)).cumsum()


def circular_list():
    p = primesto(500000)
    c = cum_sum_500k()
    l = []
    s = 1
    for i in range(400):
        for j in range(0, i - s + 1):
            x = c[i] - c[j]
            if x in p:
                if i - j > s:
                    s = i - j
                l += [[x, i - j]]
    l.sort()
    return l


def prime_maxlength_chain(n):
    if prime_maxlength_chain.cl == []:
        prime_maxlength_chain.cl = circular_list()
    cl = prime_maxlength_chain.cl
    for i in range(len(cl)):
        idx = 0
        if cl[i][0] >= n:
            idx = i - 1
            break
    l = []
    for i in range(idx, 1, -1):
        if cl[i][1] == cl[idx][1]:
            l += [cl[i][0]]
        else:
            break
    l.sort()
    return l


prime_maxlength_chain.cl = [[2, 1], [3, 1], [5, 2], [17, 4], [41, 6], [127, 9], [197, 12], [281, 14], [379, 15], [491, 15], [499, 17], [563, 17], [857, 19], [953, 21], [1151, 23], [1259, 25], [1361, 25], [1583, 27], [1823, 27], [2069, 27], [2099, 29], [2399, 31], [2417, 33], [2579, 35], [2897, 35], [2909, 37], [3803, 39], [3821, 41], [4217, 43], [4421, 43], [4651, 45], [4871, 45], [5107, 47], [5333, 47], [5813, 49], [6053, 49], [6079, 53], [6599, 55], [7699, 60], [8273, 61], [8893, 64], [9521, 65], [10181, 65], [10859, 65], [11597, 71], [12329, 71], [12713, 73], [13099, 75], [13877, 75], [14669, 75], [15527, 79], [16823, 81], [18131, 81], [19013, 81], [21407, 85], [22037, 95], [22039, 96], [24133, 100], [25237, 102], [28087, 103], [28099, 105], [28687, 105], [28697, 108], [31729, 111], [32353, 114], [33623, 115], [34913, 117], [36217, 117], [36871, 117], [37561, 122], [38921, 124], [41017, 125], [42451, 125], [42463, 127], [43201, 130], [44683, 132], [47711, 133], [49253, 133], [49279, 137], [52517, 141], [54167, 143], [55837, 146], [61027, 152], [64613, 155], [66463, 158], [70241, 162], [76099, 163], [78121, 165], [78139, 167], [79151, 167], [81203, 169], [84313, 171], [86453, 178], [92951, 183], [101999, 191], [102001, 192], [109147, 198], [115279, 201], [116531, 203], [116533, 204], [119069, 206], [121631, 208], [129419, 214], [132059, 216], [137477, 217], [138863, 219], [141671, 221], [147347, 221], [148817, 225], [153137, 225], [154579, 225], [157489, 225], [157561, 229], [157579, 231], [162007, 231], [163483, 231], [164963, 231], [164999, 233], [166541, 237], [171131, 239], [172687, 241], [175781, 241], [178889, 241], [182009, 241], [182099, 247], [182107, 249], [198197, 251], [199831, 251], [201599, 257], [203279, 259], [204979, 261], [210053, 261], [213461, 261], [213533, 267], [215261, 267], [218749, 269], [222269, 273], [225821, 273], [225829, 275], [240353, 279], [240371, 281], [240379, 283], [242243, 283], [244109, 283], [251609, 285], [255443, 291], [257353, 291], [263171, 296], [269069, 297], [281023, 299], [283079, 305], [287137, 308], [303643, 309], [303691, 313], [305783, 313], [310019, 317], [314267, 317], [318557, 321], [324991, 321], [325009, 323], [325019, 326], [329401, 328], [333821, 330], [338279, 332], [342761, 334], [351811, 335], [354097, 337], [356387, 339], [360977, 341], [360979, 342], [370261, 343], [372607, 345], [379667, 350], [393961, 356], [398771, 358], [408479, 359], [423257, 361], [423287, 363], [425819, 365], [428339, 365], [433421, 367], [433439, 369], [438521, 369], [441101, 373], [448859, 375], [448867, 377], [477809, 377], [478001, 387], [483377, 389], [496877, 391], [499607, 393]]
