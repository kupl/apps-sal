def max_consec_zeros(n):
    return 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twelve'.split()[max(map(len, bin(int(n))[2:].split('1')))]
