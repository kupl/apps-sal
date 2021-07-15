def well(arr):
    bad1 = 0
    good = 0
    for i in arr:
        for j in i:
            if str(j).lower() == "bad":
                bad1+=1
            if str(j).lower() == "good":
                good+=1
    if 0 < good < 3:
        return "Publish!"
    if good > 2:
        return "I smell a series!"
    if good == 0:
        return "Fail!"
          
            
    

