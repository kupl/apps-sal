#Function for calculating highest num
def max_value(a):
    high = a[1]
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            if ((a[x] > a[y]) and (a[x] > high) ):
                high = a[x]
                continue
            elif((a[x] < a[y]) and (a[x] > high)):
                high = a[y]
            else:
                continue
    if(a[len(a)-1] > high):
        return a[len(a)-1]
    else:
        return high

#Function for calculating Lowest num
def min_value(a):
    min = a[1]
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            if ((a[x] < a[y]) and (a[x] < min) ):
                min = a[x]
                continue
            elif((a[x] > a[y]) and (a[x] < min)):
                min = a[y]
            else:
                continue
    if(a[len(a)-1] < min):
        return a[len(a)-1]
    else:
        return min
        
#Function for Addition without highest and smallest number      
def sum_array(arr):
    #your code here
    total = 0    #Sum
    max_occ = 0 #Tells if highest num already occured 
    min_occ = 0 #Tells if lowest num already occured
    if not arr:
        return 0
    elif(len(arr) == 1):
        return 0
    else:
        for i in range(len(arr)):
            if(arr[i] == max_value(arr) and max_occ == 0):
                max_occ = 1
                continue
            if(arr[i] == min_value(arr) and min_occ == 0):
                min_occ = 1
                continue
            
            
            total = total + arr[i]

    return total
