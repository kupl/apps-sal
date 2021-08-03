def membership(amount, platinum, gold, silver, bronze):
    def res(i):
        return 'PGSBNloiroallottdvn i ezan re u   mm   e    m    b    e    r'[i::5].strip()
    for i in range(4, 0, -1):
        if (eval('apgsbmloiroalloutdvnni eztn re u    m   '[0::5])
                < eval('apgsbmloiroalloutdvnni eztn re u    m   '[i::5])):
            return res(i)
    return res(0)
