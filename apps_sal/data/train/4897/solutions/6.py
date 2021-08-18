def binary_gcd(x, y):

    while(y):
        x, y = y, x % y

    binaryx = bin(abs(x))
    bingcd = binaryx.replace('0b', '')
    return(sum(int(i) for i in bingcd))
