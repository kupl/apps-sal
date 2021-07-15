def number(bs):
    on=0
    off=0
    for i in bs:
        on+=i[0]
        off+=i[1]
    return on-off
