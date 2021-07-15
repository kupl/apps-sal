def password(string):
    #your code here
    k1 = k2 = k3 = 0
    if len(string) < 8:
        return False
    
    for i in string:
        if i.islower():
            k1 = 1
    for i in string:
        if i.isupper():
            k2 = 1
    for i in string:
        if i.isdigit():
            k3 = 1
    if k1 == k2 == k3 == 1:
        return True
    else:
        return False
