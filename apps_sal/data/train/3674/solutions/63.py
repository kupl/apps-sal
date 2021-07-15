def add_binary(int1=0, int2=1):
    bin1 = bin(int1)
    bin2 = bin(int2)
    int_sum = int(bin1, 2) + int(bin2, 2)
    bin_sum = bin(int_sum)
    return bin_sum[2:]
