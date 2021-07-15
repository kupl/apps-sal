def dec_to_binary(n, n_bits=8):
    bin_list=[]
    x=n
    while x>0:
        bit=x%2
        print(x, bit)
        bin_list.append(bit)
        print(bit)
        x//=2
    return bin_list


def evil(n):
    if dec_to_binary(n).count(1)%2==1:
        return "It's Odious!"
    else:
        return "It's Evil!"
