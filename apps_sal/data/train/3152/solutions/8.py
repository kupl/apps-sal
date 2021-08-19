def interpreter(tape, array):
    curloc = 0
    ret = list(array)
    while True:
        for x in tape:
            if curloc == len(array):
                return ''.join(ret)
            elif int(x):
                ret[curloc] = str(1 ^ int(ret[curloc], 2))
            else:
                curloc += 1
