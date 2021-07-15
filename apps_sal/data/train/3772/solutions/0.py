import re


def translate_with_frame(dna, frames=[1, 2, 3, -1, -2, -3]):
    AAs = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Base1 = 'TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
    Base2 = 'TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
    Base3 = 'TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
    trans = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    intab = "AGTC"
    outtab = "TCAG"
    map = dict()
    for i, c in enumerate(AAs):
        code = Base1[i]+Base2[i]+Base3[i]
        map[code] = c
    res = []
    for i in frames:
        trantab = dna.maketrans(intab, outtab)
        DNA = dna if i > 0 else dna[::-1].translate(trantab)
        res.append(''.join(map[x]
                           for x in re.findall(r'.{3}', DNA[abs(i)-1:])))
    return res

