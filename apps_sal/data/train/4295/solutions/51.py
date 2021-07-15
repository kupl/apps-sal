def balanced_num(numbers):
    args=[]
    string_n=str(numbers)
    for i in string_n:
        args.append(int(i))
    last_index=len(args)-1 # get the last index number of the list
    if len(args)%2==0:
        first_index=last_index//2 # get the indexs of two characters in the middle of the list
        second_index=last_index//2+1
        if sum(args[0:first_index])==sum(args[second_index+1:]): #use slice to get characters from left and right side 
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        index=last_index//2
        if sum(args[0:index])==sum(args[index+1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
