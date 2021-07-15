def string_counter(string, char):
    num=0
    for i in range(len(string)):
        if string[i]==char:
            num+=1
    return num
