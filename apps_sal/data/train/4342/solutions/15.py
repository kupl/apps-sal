def no_space(x):
    #your code here
    list = x.split()
    a = ""
    for i in range(len(list)):
        a = a + list[i]
    return a    
