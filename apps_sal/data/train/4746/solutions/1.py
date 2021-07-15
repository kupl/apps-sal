def fisHex(name):
    # fish is 15
    hexdict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    res=0
    for c in name.upper():
        if c in hexdict:
          res^=hexdict[c]
    return res

