def count_deaf_rats(town):
    total = 0
    town = town.replace(" ", "")
    print(town)
    town = town.split("P")
    print(town)
    if '' in town:
        for i in range(len(town)):
            if town[i] != "" and i == 0:
                town[i] = list(town[i])
                for j in range(0, len(town[i]), 2):
                    print((''.join(town[i][j:j+2])))
                    
                    if ''.join(town[i][j:j+2]) == "O~":
                        
                        total += 1
            elif town[i] != "" and i == 1:
                town[i] = list(town[i])
                for j in range(0, len(town[i]), 2):
                    if ''.join(town[i][j:j+2]) == "~O":
                        total += 1
                
        return total
    else:
        for i in range(len(town)):
            if i == 0:
                town[i] = list(town[i])
                for j in range(0, len(town[i]), 2):
                    print((town[i][j:j+2]))
                    if ''.join(town[i][j:j+2]) == "O~":
                        print(j)
                        total += 1
            else:
                town[i] = list(town[i])
                for j in range(0, len(town[i]), 2):
                    if ''.join(town[i][j:j+2]) == "~O":
                        print(j)
                        total += 1
        return total
            
          
              
                    
              
    
    

