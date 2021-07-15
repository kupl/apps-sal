def lowercase_count(string):
    sum = 0
    for i in string:
        if i.islower():
            sum+=1
    return sum
