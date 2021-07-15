def order_weight(strng):
    strng_list = strng.split(" ")
    lst = list(zip(map(lambda x: sum(int(i) for i in x),strng_list),strng_list))
    stl = list(map(lambda x: x[1],sorted(lst,key=lambda x: (x[0],x[1]))))
    return " ".join(s for s in stl)
