def maximum_product_of_parts(n):
    ns = str(n)
    return max(int(ns[:b])*int(ns[b:c])*int(ns[c:]) for a in range(len(ns)-2) for b in range(a+1,len(ns)-1) for c in range(b+1,len(ns)))

