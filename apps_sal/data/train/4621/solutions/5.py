def count_deaf_rats(town):
    town = town.replace(" ", "")
    left,p,right = town.partition("P")
    left = replace_rats(left)
    right = replace_rats(right)
    return left.count("L") + right.count("R")

#no clean way to use string replace, step through string 2 chars at a time
def replace_rats(rats):
    ret_array = []
    for x in range(0, len(rats), 2):
        if rats[x] == '~':
            ret_array.append('R')
        else:
            ret_array.append('L')
    return ret_array
