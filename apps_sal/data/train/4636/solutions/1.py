M1 = "abcde123fghij456klmno789pqrst.@0uvwxyz_/° "
M2 = "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/° "
M3 = "^~?!\'\"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡°°°_/° "

D1 = {c: divmod(i, 8) for i, c in enumerate(M1)}
D2 = {c: divmod(i, 8) for i, c in enumerate(M2)}
D3 = {c: divmod(i, 8) for i, c in enumerate(M3)}
D = (D1, D2, D3)


def dist(i, j, k, l): return min(abs(i - k), 6 - abs(i - k)) + min(abs(j - l), 8 - abs(j - l)) + 1


def tv_remote(words):
    def rec(c, d, i, j):
        if c == len(words):
            return 0
        tmp = D[d].get(words[c])
        if tmp:
            return dist(i, j, *tmp) + rec(c + 1, d, *tmp)
        return dist(i, j, 5, 0) + rec(c, (d + 1) % 3, 5, 0)
    return rec(0, 0, 0, 0)
