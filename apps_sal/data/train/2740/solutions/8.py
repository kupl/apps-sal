def wheat_from_chaff(values):
    last_index=len(values)-1
    for i in range(0, len(values)):
        if values[i] > 0:
            negative_index = None
            negative_value = None
            for ii in range(last_index, -1, -1):
                if values[ii] < 0:
                    last_index = ii
                    negative_index = ii
                    negative_value = values[ii]
                    break
            if(negative_index == None):
                break
            elif(negative_index > i):
                values[i], values[ii] = values[ii], values[i]
            else:
                break
    return values  
                
                
            

