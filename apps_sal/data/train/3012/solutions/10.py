def shared_bits(a, b):
    if a > b:
        c=a
        a=b
        b=c 
    a_bin = str(bin(a))
    b_bin = str(bin(b))
    count = 0
    for i in range(len(a_bin)-1,1,-1):
        if a_bin[i] == '1' and a_bin[i]==b_bin[i+len(b_bin)-len(a_bin)]:
            count += 1
    if count >= 2:
        return True
    else:
        return False
