def combs(comb1, comb2):
    c1 = int(comb1.replace('*', '1').replace('.', '0'), 2)
    c2 = int(comb2.replace('*', '1').replace('.', '0'), 2)
    def r(x, y):
        if x.__xor__(y) == x + y:
            return max(x.bit_length(), y.bit_length())
        return r(x<<1,y)
    return min(r(c1,c2), r(c2,c1))
