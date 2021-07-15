def well(arr):
    c = len([j for i in arr for j in i if str(j)[0] in "Gg"])
    if c == 0: return "Fail!"
    elif c <= 2: return "Publish!"
    else: return "I smell a series!"
    

