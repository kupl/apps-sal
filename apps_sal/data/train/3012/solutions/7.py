def shared_bits(a, b):
    res=0
    bina,binb='{:b}'.format(a),'{:b}'.format(b)
    bina,binb=bina.zfill(max(len(bina),len(binb))),binb.zfill(max(len(bina),len(binb)))
    for x,y in zip(bina,binb):
        if x==y=='1':
            res+=1
            if res==2:
                return True
    return False
