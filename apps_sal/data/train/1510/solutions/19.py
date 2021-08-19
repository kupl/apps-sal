# cook your dish here
T = int(input())
while T > 0:
    s = str(input())
    T = T - 1
    L = list(s)
    Pa = L.index("A")
    Pb = L.index("B")
    Pc = L.index("C")
    Pd = L.index("D")
    Pe = L.index("E")
    Pf = L.index("F")
    Pg = L.index("G")
    Ph = L.index("H")
    Pi = L.index("I")
    Pj = L.index("J")
    List = [Pa, Pb, Pc, Pd, Pe, Pf, Pg, Ph, Pi, Pj]
    A = max(List)
    print(A + 1)
