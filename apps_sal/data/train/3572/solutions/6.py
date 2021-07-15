def invite_more_women(arr):
    freq = {}
    for item in arr: 
        if (item in freq): 
            freq[item] += 1 
        else: 
            freq[item] = 1 
    print(freq)
    if 1 not in freq:
        return False
    if -1 not in freq: 
        return True
    if freq[1] == freq[-1]: 
        return False
    if freq[1] > freq[-1]: 
        return True
    else: 
        return False
