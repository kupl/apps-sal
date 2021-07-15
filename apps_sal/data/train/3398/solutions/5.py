def solve(arr):

    head = arr[0]
    tail = arr[-1]
    
    check = [(i,j) for i in range(head-1,head+2) for j in range(tail-1,tail+2)]
    
    possibles = []
    for start, end in check:
        if (end-start)%(len(arr)-1) == 0:
            possibles.append((start,end))
    
    global_changes = float('inf')
    
    for start, end in possibles:
        
        diff = int((end-start)/(len(arr)-1))
        
        if diff == 0: tester = [start]*len(arr)
        else: tester = list(range(start, end+diff, diff))
        
        current_changes = 0
        
        for i in range(len(tester)):
            if abs(tester[i] - arr[i]) > 1:
                current_changes = float('inf')
                break
            elif abs(tester[i] - arr[i]) == 1:
                current_changes += 1
        
        global_changes = min(current_changes, global_changes)
                
    
    return global_changes if global_changes != float('inf') else -1
