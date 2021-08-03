def get_diagonale_code(s):
    S = [x.split()for x in s.split('\n')]
    i, z, L = 0, '', list(range(len(S)))
    while 1:
        try:
            for j in L + L[1:-1][::-1]:
                z, i = z + S[j][i], i + 1
        except:
            return z
