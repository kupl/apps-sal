def order_weight(strng):
    if len(strng) > 1:
        stg = strng.split()
        k = []
        for i in stg:
            l = 0
            for m in i:
                l += int(m)
            k.append(l)
        q = list(zip(k, stg))
        q.sort(key=len, reverse=True)
        p = sorted(q, key=lambda t: (t[0], t))
        print(p)
        v = list(zip(*p))
    # print(v[1])
        return " ".join(v[1])
    else:
        return strng

# def getsum(stg):
#    k = []
 #   for i in stg:
  #       l = 0
   #     for m in i:
  #          l += int(m)
    #    k.append(l)
# have this fns take a number as an input and output the sum of the digits
