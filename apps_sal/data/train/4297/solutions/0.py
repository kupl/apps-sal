def get_mean(arr,x,y):
    if 1 < x <= len(arr) and 1 < y <= len(arr):
       return (sum(arr[:x])/x+sum(arr[-y:])/y)/2
    return -1
