def reverse_list(l):
    arr=[]
    for i in range(len(l)):
        arr.append(l[len(l)-1-i])
    return arr
