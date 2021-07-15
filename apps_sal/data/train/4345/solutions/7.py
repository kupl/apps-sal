def buy_or_sell(pairs,f):
    out=[]
    for pair in pairs:
        if pair[0]==f:
            f=pair[1]
            out.append("buy")
        elif pair[1]==f:
            f=pair[0]
            out.append("sell")
        else:return "ERROR"
    return out
