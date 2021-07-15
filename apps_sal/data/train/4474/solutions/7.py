from math import log
def start_smoking(bars,boxes):
    n=(bars*10+boxes)*18
    stubs=n
    while stubs>4:
        n+=stubs//5
        stubs=sum(divmod(stubs,5))
    return n
