def balanced_num(number):
    number1 = str(number)
    SliceNumber = int((len(number1)-1)/2)
    Left_Of_Middle = list(number1[:SliceNumber])
    Right_Of_Middle = list(number1[len(number1)-SliceNumber:])
   
    Left_Of_Middle = list(map(int, Left_Of_Middle))
    Right_Of_Middle = list(map(int, Right_Of_Middle))

    if sum(Left_Of_Middle) == sum(Right_Of_Middle):
        return("Balanced")
    else:
        return("Not Balanced")
