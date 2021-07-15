def encode(m, k):
    k = map(int, (str(k)*(len(m)//len(str(k))+1))[:len(m)])
    return list(map(sum,zip([ord(x)-96 for x in m],k)))
