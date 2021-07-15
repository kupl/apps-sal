import collections
def primeFactors(n):
    ret = []
    pows = {}
    st = ""
    i = 2
    while(i<n):
        if n%i == 0:
            n /= i
            ret.append(i)
        else:
            i += 1
    ret.append(int(n))
    for j in set(ret):
        pows.update({int(j):ret.count(j)})
    print(pows)
    pows = collections.OrderedDict(sorted(pows.items()))
    for key in pows:
        if pows[key] > 1:
            st += "("+ str(key)+"**"+ str(pows[key])+")"
        else:
            st += "("+str(key)+")"
    return st
