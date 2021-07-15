def to_bits(string):
    
    input=sorted([int(x) for x in string.split("\n")])
    bitmap=[0]*5000
    for i in input:
        bitmap[i]=1
    return bitmap
