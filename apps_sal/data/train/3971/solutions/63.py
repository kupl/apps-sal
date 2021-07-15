def tidyNumber(n):
    new_string = str(n)
    count = 0
    for i in range(0, len(new_string)-1):
        if new_string[i]<=new_string[i+1]:
            count+=1
    return count == len(new_string)-1
