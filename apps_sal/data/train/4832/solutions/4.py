def all_non_consecutive(arr): #define the function
    start = 0 #This is a variable which will detect if the number is the first in the list. In that case it won't have a preceding number to be consecutive to it
    answer = [] #empty list for later use. This will be the list which will contain the answer, i.e, where we will append the non consecutive entries
    for number in arr: #for loop goes through each entry in the list because we want to check the non consecutive numbers in it
        if start == 0: #as mentioned before start is a variable set to check if the number presented is the first in the list. If yes, it satisfies the equation
            current = number #current is a variable which is used to take the number as current after all processes so we can check if the next number is 1 extra than it
            start = 1 #changes start to 1 so we know that next values aren't first in the list and this never satisfies the if loop after this
            continue #goes to the start of the start of the loop because it the first number doesn't need to go further
        elif number != current + 1: #we ignore the consecutive numbers and if the number in the loop right now is not one more than the previous one, this situation is triggered
            format = {'i' : arr.index(number), 'n' : number} #format is a dictionary which assigns the items and numbers in a format the program wants
            answer.append(format) #we append the dictionary in the list which will give the answer because the answer needs to be in a list form
        current = number #same as used before
    return answer #we done and dusted and return finishes the process. YAY!

