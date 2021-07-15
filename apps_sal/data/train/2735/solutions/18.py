def jumping_number(number):
    arr_number=[int(i) for i in str(number)]
    for x in range(len(arr_number)-1):  
        if abs(arr_number[x] - arr_number[x+1]) !=1: 
            return "Not!!"      
    return "Jumping!!"
