LST,M = [0,2,3,18,11],12345787

def gen3N():
    Ae,Be,Ao,Bo,Co = 3,8,4,8,6
    while 1:
        Ae,Be, Ao,Bo,Co = [ v%M for v in (Ae+Be, 2*Ae+3*Be ,
                                          Be+Ao+Bo+Co, Be+2*Ao+3*(Bo+Co), 2*(Ae+Be) ) ]
        yield (n%M for n in (Ao+Bo+Co,Ae+Be))

GEN = gen3N()

def three_by_n(n):
    while len(LST) <= n: LST.extend(next(GEN))
    return LST[n]
