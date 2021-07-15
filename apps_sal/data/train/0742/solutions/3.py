def SR(coeff):
    size = len(coeff) # Please work out what if n is small no, like 1 or 2
    #print("No. of rows will form is", size)
    max_power = size - 1
    Arr = [] # 2x2
    row1 = coeff[0::2]
    row2 = coeff[1::2]
    #print('row1: ', row1, '\n', 'row2: ', row2)
    ln = len(row1) #don't change this value
    if size%2 != 0: # if n is odd
        row2.append(0) # to balance row1 and row2
    # add 1 empty element in each row for safety
    row1.append(0) 
    row2.append(0) 
    Arr.append(row1)
    Arr.append(row2)
    #print('start')
    
    sign = lambda x: 1 if x > 0 else -1  
    s = [sign(row1[0]), sign(row2[0])] # keep track of sign of 1st member of each row
    
    for r in range(2,size):
        Arr.append([0]*(ln+1)) # create a row of empty elements
        #print(r+1,'th row created', Arr)
        
        for n in range(ln): #generate value of nth element of rth row
            #print(n+1, 'th element to fill')
            # below mean, (12 * 4) - (10*5)
            Arr[r][n] = (Arr[r-1][0] * Arr[r-2][n+1]) - (Arr[r-2][0] * Arr[r-1][n+1])
            
        
        s.append(sign(Arr[r][0]))
        #print("  Array Print:  ")
        #for k in Arr: print(k) 
        
    ''' If all the element of that row is zero case
    then nth element = nth element of its previous row *
    ((max. power of x) - 4 - r - 2n ) '''
    for i in range(len(Arr)): # i th row in Arr
        if list(set(Arr[i])) == [0]:       
            #print(Arr[i])
            for n in range(len(Arr[i])):
                # I think that make sense
                Arr[i][n] = (Arr[i-1][n] * (max_power + 4 - (i+1) - (2*(n+1))))
                
        elif Arr[i][0] == 0:
            return 0 
        
    ''' check if sign change '''
    if len(set(s)) == 1: # no sign change
        return 1
    else: # sign change
        return 0

            
          
T = int(input())
#coeff = [10, 12, 4, 5, 3, 2]
for t in range(T):
    coeff = [int(x) for x in input().split()] # [10, 12, 4, 5, 3]
    print(SR(coeff))
