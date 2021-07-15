def str_count(strng, letter):
    sum=0
    for i in range(0,len(strng)):
        if letter==strng[i]: sum+=1
    return sum

