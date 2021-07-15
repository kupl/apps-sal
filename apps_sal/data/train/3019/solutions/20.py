def str_count(strng, letter):
    x=0
    for i in range(len(strng)):
        if strng[i]==letter:
            x+=1
    return x 
