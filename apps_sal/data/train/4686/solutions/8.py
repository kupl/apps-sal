def double_every_other(lst):
    return [num*2 if index % 2 != 0 else num for index,num in enumerate(lst)]
