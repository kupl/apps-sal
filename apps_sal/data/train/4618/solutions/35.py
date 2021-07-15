def positive_sum(arr):#function declaration
    sum=0             #instiallization of zero
    for i in arr:     # for loop to check the integers in the array
        if i>0:       # condiation
            sum=sum+i #This condiation will add all the numbers>0
    return sum        #will give sum of all the positive integres

