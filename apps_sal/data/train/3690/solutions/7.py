def solve(st, idx):
    #If char at index is not an opening bracket, return -1
    if st[idx] != "(":
        return -1
    #Create a stack data structure
    stack = []
    for i in range(len(st)):
        #If the char at our current index i is an opening bracket, push index on our stack
        if st[i] == "(":
            stack.append(i)
        #If the char is a closing bracket, pop from our stack
        elif st[i] == ")":
            tmp = stack.pop()
            #If the value from our stack matches the given idx, then our current index i is 
            #the closing bracket we are searching for, thus we return said index i
            if tmp == idx:
                return i
    #If there was no solution, return -1
    return -1

