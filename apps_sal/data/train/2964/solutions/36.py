def sum_two_smallest_numbers(numbers):
    #your code here
    min1=0
    min2=0
    max=0
 
    for x in numbers:
        if x>=max:    
            max=x
    min1=max
    for y in numbers:
        if y<min1:
            min1=y

    min2=max
    for z in numbers:
        if z <min2:
            if z!=min1:
                min2=z

         
    print ( numbers )
    print(("Maximo =" , max))
    print(("Minimo 1=" , min1 ))
    print(("Minimo 2=" , min2 ))
    returnVal=min1+min2
    print(("Suma=" , returnVal ))           
    return returnVal

