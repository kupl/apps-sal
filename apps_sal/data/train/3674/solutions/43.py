def add_binary(a,b):
    c = bin(a + b)
    bin_c = ""
    bin_lst=[]
    for char in c:
        bin_lst.append(char)
    for num in bin_lst[2:len(bin_lst)]:
        bin_c += num
    return bin_c
