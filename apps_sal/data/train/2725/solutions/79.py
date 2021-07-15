def gimme(arr):
    return len(arr) - (arr.index(max(arr)) + arr.index(min(arr)))    
