def lowercase_count(strng):
    # Your code here
    count = 0
    s = [i for i in strng]
    for x in s:
        if x.islower() == True:
            count += 1
        else:
            pass
    return count
        

