def is_sorted_and_how(arr):

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            print(str(arr[i]) + ' ' +  str(arr[i+1]))
    

    as_start = 0
    de_start = 0
    
    def compare(first,second):
        if second > first:
            return 'as'
        elif first > second:
            return 'de'
        else:
            return 'eq'
          
    state = compare(arr[0],arr[1])
    
    for i in range(1,len(arr)-1):
        
        
        
        new_state = compare(arr[i],arr[i+1])
        
        print(f"{arr[i]}, {arr[i+1]}, {new_state}, {state}")
        
        if new_state != 'eq':
            
            if state == 'eq':
                state = new_state
            
            if new_state != state:
                state = 'unsorted'
                break
        

    if state == 'unsorted' or  state =='eq':
        return 'no'
    if state == 'as':
        return 'yes, ascending'
    if state == 'de':
        return 'yes, descending'
