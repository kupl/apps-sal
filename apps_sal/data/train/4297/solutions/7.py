def get_mean(arr,x,y):
    return -1 if min(x,y) < 2 or max(x,y) > len(arr) else (sum(arr[:x])/x + sum(arr[-y:])/y)/2
