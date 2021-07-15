def count_deaf_rats(town):
    piper = False
    count = 0
    expectedChar = '~'
    deafRats = 0
    
    while count < len(town):
        if town[count] == ' ':
            count += 1
            
        elif town[count] == expectedChar:
            count += 2
            
        elif town[count] == 'P':
            piper = True
            expectedChar = 'O'
            count += 1
        
        else:
            deafRats += 1
            count += 2
                
    return deafRats

