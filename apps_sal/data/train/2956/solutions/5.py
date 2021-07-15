def encode(string):
    return ''.join([(i*3) for i in ''.join([(bin(i)[2:]).zfill(8) for i in [ord(i) for i in string]])])

def decode(bits):
    three = [i for i in bits]
    for i in range(3,len(bits)//3*4,4): three.insert(i,' ')
    three = ''.join(three).split()
    binar = ['0' if i.count('0')>i.count('1') else '1' for i in three]
    for i in range (8,len(binar)//8*9,9): binar.insert(i,' ')
    binar = ''.join(binar).split()
    asci = [int(i,2) for i in binar]
    string = ''.join([chr(i) for i in asci])
    return string
