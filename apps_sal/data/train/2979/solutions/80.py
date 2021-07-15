def get_age(age):
    #your code here
    
    res = [int(i) for i in age.split() if i.isdigit()]
    return res[0]
