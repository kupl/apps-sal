def well(x):
    
    c= x.count("good")
    if c < 1:
        return "Fail!"
    elif 1 <= c <=2 :
        return "Publish!"
    else:
        return "I smell a series!"
        

