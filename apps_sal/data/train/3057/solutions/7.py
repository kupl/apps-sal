def is_bouncy (n):
    num_list = [int (x) for x in str (n)]
    up = down = False
    for index in range (1, len (num_list)):
        if (num_list[index-1] < num_list[index]):
           up = True
        elif (num_list[index-1] > num_list[index]):
           down = True
        if (up and down):
           return True
    return False
