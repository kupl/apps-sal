def dont_give_me_five(start,end):
    mylist = [str(i) for i in range(start, end+1)]
    mylist = [i for i in mylist if '5' not in i]
    return len(mylist)
