def tidyNumber(n):
    num_str = str(n)
    for x in range(len(num_str)-1):
        if int(num_str[x]) > int(num_str[x+1]):
            return False
    return True
