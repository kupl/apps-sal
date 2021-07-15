def solve(msg):
    l = 'abcdefghijklmnopqrstuvwxyz'
    U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    msg = list(msg)
    lc,Uc = 0,0
    for i in range(len(msg)):
        if msg[i] in l:
            lc += 1
        if msg[i] in U:
            Uc += 1
    if lc > Uc or lc == Uc:
        return ''.join(msg).lower()
    else:
        return ''.join(msg).upper()

