def find_in_array(seq, predicate): 

    for index, value in enumerate(seq):
        if predicate(value,index):
            return index
    return -1 



#     print(type(predicate)) #function
#     print(type(seq)) #list
#     print(predicate.__name__) lambda

