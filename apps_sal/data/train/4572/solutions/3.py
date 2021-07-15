def max_consec_zeros(n):
    w = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen'.split()
    return w[max(map(len, bin(int(n))[2:].split('1')))]
