def invite_more_women(arr):
    men = 0
    women = 0
    
    for elem in arr:
        if elem == -1:
            women += 1
        elif elem == 1:
            men += 1
    
    return men > women
