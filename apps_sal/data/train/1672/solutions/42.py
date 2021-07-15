import re

s = """
per nextum in unam tum XI conscribementis fac sic
    vestibulo perlegementum da varo.
    morde varo.
    seqis cumula varum.
cis

per nextum in unam tum XI conscribementis fac sic
    seqis decumulamenta da varo.
    varum privamentum fodementum da aresulto.
    varum tum III elevamentum tum V multiplicamentum da bresulto.
    aresultum tum bresultum addementum da resulto.

    si CD tum resultum non praestantiam fac sic
        dictum sic f(%d) = %.2f cis tum varum tum resultum egresso describe.
        novumversum egresso scribe.
    cis
    si CD tum resultum praestantiam fac sic
        dictum sic f(%d) = MAGNA NIMIS! cis tum varum egresso describe.
        novumversum egresso scribe.        
    cis
cis
""".strip()
if False:
    s = re.sub(r"\bIII\b", "3", s)
    s = re.sub(r"\bV\b", "5", s)
    s = re.sub(r"\bXI\b", "11", s)
    s = re.sub(r"\bCD\b", "400", s)
    s = re.sub(r"per (.*?) fac sic(.*?)\ncis", r"for (\1) {\2\n}", s, flags=re.DOTALL)
    s = re.sub(r"\bdictum sic (.*) cis(.*) egresso describe.", r'printf("\1"\2)', s)
    s = re.sub(r"novumversum egresso scribe.", r'print("\\n")', s)
    s = re.sub(r"si (.*?) fac sic(.*?)cis", r"if (\1) {\2}", s, flags=re.DOTALL)
    s = re.sub(r".$", "", s)
    s = re.sub(r" tum ", " ", s)
    print(s)
    return

a = []
for i in range(11):
    a.append(int(input()))
for i in range(11):
    var = a.pop()
    aresult = abs(var) ** 0.5
    bresult = (var ** 3) * 5
    result = aresult + bresult
    if 400 > result:
        print("f({0:d}) = {1:.2f}".format(var, result))
    else:
        print("f({0:d}) = MAGNA NIMIS!".format(var))

