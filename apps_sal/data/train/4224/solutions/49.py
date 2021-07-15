def dont_give_me_five(start,end):
    return len([i for i in range(start, end+1) if not '5' in str(i)])
    
    # numbers_list = []
    # for i in range(start, end+1):
    #     if not '5' in str(i):
    #         numbers_list.append(i)
    # return len(numbers_list)

