def buy_or_sell(p, hf):
    act = []
    for f in p:
        if hf not in f:
            return "ERROR"
        elif hf == f[0]:
            act.append("buy")
            hf = f[1]
        else:
            act.append("sell")
            hf = f[0]
    return act
